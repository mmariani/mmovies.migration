#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import itertools
import os
import re
import sys
import time

import pymongo

import logging

log = logging.getLogger(__name__)


class ParsingError(Exception):
    pass


HOST = '127.0.0.1'
PORT = 27017

# XXX look for tabs within imported fields - they might need to be split further
# XXX use a real parser, will we?


def forward_stream(stream, re_guard):
    """
    Returns the part of a stream file after the 're_guard' regular expression matches a complete line,
    then skips lines that are blank or composed by '=' characters.
    """

    for rawline in stream:
        if re.match('^%s$' % re_guard, rawline):
            while True:
                first = next(stream)
                if not re.match('(=*|)\n', first):
                    break
            break
    else:
        raise ParsingError("Cannot parse: %s does not contain the line '%s'" % (stream.name, re_guard))

    return itertools.chain([first], stream)





class Loader(object):

    def __init__(self, db, plaintext_dir):
        self.db = db
        self.plaintext_dir = plaintext_dir
        self.coll_movies = self.db['movies']
        self.t0 = time.time()


    def print_progress(self, n):
        if n % 431:
            return
        n = str(n)
        sys.stdout.write(n)
        sys.stdout.write(chr(8)*len(n))
        sys.stdout.flush()


    def print_total(self, n):
        n = str(n)
        print '%s... done (%s secs).' % (n, int(time.time()-self.t0))


    def iter_list(self):
        """
        Yields stripped lines from a list of stuff, either gzipped or not (which is slightly faster).
        """
        # XXX better docstring for this one
        try:
            filename = os.path.join(self.plaintext_dir, '%s.list' % self.list_name)
            fin = open(filename, 'rb')
        except IOError:
            filename = os.path.join(self.plaintext_dir, '%s.list.gz' % self.list_name)
            fin = gzip.GzipFile(filename)

        for rawline in forward_stream(fin, self.re_guard):
            yield rawline.rstrip().decode('latin1')




class YearLoader(Loader):

    list_name = 'movies'
    re_guard = 'MOVIES LIST'

    def iter_years(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            movie_name, year = data[0], data[1].strip()
            yield movie_name, year


    def load(self):
        for idx, (movie_name, year) in enumerate(self.iter_years()):
            self.coll_movies.insert({'name': movie_name, 'year': year})
            self.print_progress(idx)

        self.print_total(idx)




class TaglinesLoader(Loader):

    list_name = 'taglines'
    re_guard = 'TAG LINES LIST'

    def iter_taglines(self):
        movie_name = None

        for line in self.iter_list():
            if line.startswith('# '):
                movie_name = line[2:]
            elif line:
                yield movie_name, line.strip()

    def load(self):
        for idx, (movie_name, taglines) in enumerate(self.iter_taglines()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'taglines': taglines}})
            self.print_progress(idx)

        self.print_total(idx)




class ProductionCompaniesLoader(Loader):

    list_name = 'production-companies'
    re_guard = 'PRODUCTION COMPANIES LIST'

    def iter_companies(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            movie_name, company_name = data[0], data[1].strip()
            yield movie_name, company_name


    def load(self):
        for idx, (movie_name, company_name) in enumerate(self.iter_companies()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'company_name': company_name}})
            self.print_progress(idx)

        self.print_total(idx)





class DistributorsLoader(Loader):

    list_name = 'distributors'
    re_guard = 'DISTRIBUTORS LIST'

    def iter_distributors(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, distributor_name = data[0], data[1].strip()
            yield movie_name, distributor_name


    def load(self):
        for idx, (movie_name, distributor_name) in enumerate(self.iter_distributors()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'distributors': distributor_name}})
            self.print_progress(idx)

        self.print_total(idx)



class LocationsLoader(Loader):

    list_name = 'locations'
    re_guard = 'LOCATIONS LIST'

    def iter_locations(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            movie_name, locations = data[0], data[1].strip()
            yield movie_name, locations


    def load(self):
        for idx, (movie_name, locations) in enumerate(self.iter_locations()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'locations': locations}})
            self.print_progress(idx)

        self.print_total(idx)




class MiscellaneousCompaniesLoader(Loader):
    # XXX refactor see locations

    list_name = 'miscellaneous-companies'
    re_guard = 'MISCELLANEOUS COMPANY LIST'

    def iter_companies(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            movie_name, companies = data[0], data[1].strip()
            yield movie_name, companies


    def load(self):
        for idx, (movie_name, companies) in enumerate(self.iter_companies()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'miscellaneous-companies': companies}})
            self.print_progress(idx)

        self.print_total(idx)







class GenreLoader(Loader):

    list_name = 'genres'
    re_guard = '\d: THE GENRES LIST'

    def iter_genres(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, genre = data[0], data[1].strip()
            yield movie_name, genre


    def load(self):
        for idx, (movie_name, genre) in enumerate(self.iter_genres()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'genre': genre}})
            self.print_progress(idx)

        self.print_total(idx)



class LanguageLoader(Loader):

    list_name = 'language'
    re_guard = 'LANGUAGE LIST'

    def iter_languages(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            if len(data) == 1:      # missing language, it happens
                continue
            movie_name, language = data[0], data[1].strip()
            yield movie_name, language


    def load(self):
        for idx, (movie_name, language) in enumerate(self.iter_languages()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'language': language}})
            self.print_progress(idx)

        self.print_total(idx)



class CountriesLoader(Loader):

    list_name = 'countries'
    re_guard = 'COUNTRIES LIST'

    def iter_countries(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            if len(data) == 1:      # missing language, it happens
                continue
            movie_name, country = data[0], data[1].strip()
            yield movie_name, country


    def load(self):
        for idx, (movie_name, country) in enumerate(self.iter_countries()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'country': country}})
            self.print_progress(idx)

        self.print_total(idx)




class AkaTitlesLoader(Loader):

    list_name = 'aka-titles'
    re_guard = 'AKA TITLES LIST'

    def iter_aka_titles(self):
        movie_name = None
        aka_titles = []

        new_movie = True
        for line in self.iter_list():
            if new_movie:
                if movie_name:
                    yield movie_name, aka_titles
                movie_name = line
                aka_titles = []
                new_movie = False
            elif not line:
                new_movie = True
            else:
                aka_titles.append(line.strip())
        yield movie_name, aka_titles


    def load(self):
        for idx, (movie_name, aka_titles) in enumerate(self.iter_aka_titles()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'aka_titles': aka_titles}})
            self.print_progress(idx)

        self.print_total(idx)



class PlotLoader(Loader):

    list_name = 'plot'
    re_guard = 'PLOT SUMMARIES LIST'

    def iter_plot(self):
        movie_name = None
        plot_lines = []

        for line in self.iter_list():
            if line.startswith('MV: '):
                movie_name = line[4:]
                plot_lines = []
            elif line.startswith('PL: '):
                plot_lines.append(line[4:])
            elif line.startswith('BY: '):
                yield movie_name, ' '.join(plot_lines), line[4:]

    def load(self):
        for idx, (movie_name, plot, by) in enumerate(self.iter_plot()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'plot': {'text': plot, 'by': by}}})
            self.print_progress(idx)

        self.print_total(idx)



class TriviaLoader(Loader):

    list_name = 'trivia'
    re_guard = 'FILM TRIVIA'

    def consume_trivia(self, first_line, it):
        trivia_lines = [first_line[2:]]
        while True:
            line = next(it)
            if line:
                trivia_lines.append(line[2:])
            else:
                break
        return ' '.join(trivia_lines)


    def iter_trivia(self):
        movie_name = None

        it = self.iter_list()
        while True:
            line = next(it)
            if line.startswith('# '):
                movie_name = line[2:]
            elif line.startswith('- '):
                trivia = self.consume_trivia(line, it)
                yield movie_name, trivia


    def load(self):
        # TODO: separate trivia into separate attributes if they begin with 'EASTER EGG: ' or 'SPOILER: '
        for idx, (movie_name, trivia) in enumerate(self.iter_trivia()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'trivia': trivia}})
            self.print_progress(idx)

        self.print_total(idx)






class GoofsLoader(Loader):
    # XXX refactor, see Trivia

    list_name = 'goofs'
    re_guard = 'GOOFS LIST'

    def consume_goof(self, first_line, it):
        goof_lines = [first_line[2:]]
        while True:
            line = next(it)
            if line:
                goof_lines.append(line[2:])
            else:
                break
        return ' '.join(goof_lines)


    def iter_goof(self):
        movie_name = None

        it = self.iter_list()
        while True:
            line = next(it)
            if line.startswith('# '):
                movie_name = line[2:]
            elif line.startswith('- '):
                goof = self.consume_goof(line, it)
                yield movie_name, goof


    def load(self):
        # XXX divide into CHAR, CONT, CREW, FACT, FAIR, FAKE, PLOT, SYNC

        for idx, (movie_name, goof) in enumerate(self.iter_goof()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'goofs': goof}})
            self.print_progress(idx)

        self.print_total(idx)







class ColorInfoLoader(Loader):

    list_name = 'color-info'
    re_guard = 'COLOR INFO LIST'

    def iter_colorinfo(self):
        for line in self.iter_list():
            if set(line) == set(['-']):     # empty line, discarded
                continue
            data = line.split('\t', 1)
            movie_name, color_info = data[0], data[1].strip()
            yield movie_name, color_info

    def load(self):
        for idx, (movie_name, color_info) in enumerate(self.iter_colorinfo()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'color_info': color_info}})
            self.print_progress(idx)

        self.print_total(idx)




def main(plaintext_dir):
    conn = pymongo.Connection(HOST, PORT)

    db = conn['imdb']

    # purge the old data before loading
    db.drop_collection('movies')

    coll_movies = db['movies']
    coll_movies.create_index([("name", pymongo.ASCENDING)])

    for loader_factory in [
            YearLoader,
            TaglinesLoader,
            ProductionCompaniesLoader,
            GenreLoader,
            LanguageLoader,
            CountriesLoader,
            AkaTitlesLoader,
            PlotLoader,
            TriviaLoader,
            ColorInfoLoader,
            GoofsLoader,
            DistributorsLoader,
            MiscellaneousCompaniesLoader,
            LocationsLoader,
        ]:
        loader = loader_factory(db=db, plaintext_dir=plaintext_dir)
        print 'loading %s' % loader.list_name
        loader.load()


