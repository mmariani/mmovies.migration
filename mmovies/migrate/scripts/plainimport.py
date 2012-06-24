#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import itertools
import os
import re
import sys

import pymongo

import logging

log = logging.getLogger()


class ParsingError(Exception):
    pass



HOST = '127.0.0.1'
PORT = 27017




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
        raise ParsingError("Bad stream: %s does not contain the line '%s'" % (stream.name, re_guard))

    return itertools.chain([first], stream)










def humancount(n):
    n = float(n)
    if n >= 10**6:
        return '%.1fM' % (n / 10**6)
    elif n >= 1**3:
        return '%.1fk' % (n / 10**3)
    else:
        return '%d' % n






class Loader(object):

    def __init__(self, db, plaintext_dir):
        self.db = db
        self.plaintext_dir = plaintext_dir
        self.coll_movies = self.db['movies']


    def print_progress(self, n):
        n = str(n)
        sys.stdout.write(n)
        sys.stdout.write(chr(8)*len(n))
        sys.stdout.flush()


    def print_total(self, n):
        n = str(n)
        sys.stdout.write(n)
        sys.stdout.write('... done.')
        sys.stdout.flush()


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

        print 'parsing %s' % filename
        for rawline in forward_stream(fin, self.re_guard):
            yield rawline.strip().decode('latin1')







class YearLoader(Loader):

    list_name = 'movies'
    re_guard = 'MOVIES LIST'

    def iter_years(self):
        for line in self.iter_list():
            data = line.split('\t')
            movie_name, year = data[0], data[-1]
            yield movie_name, year


    def load(self):
        for idx, (movie_name, year) in enumerate(self.iter_years()):

            movie = {
                    'name': movie_name,
                    'year': year
                    }

            self.coll_movies.insert(movie)

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print




class TaglinesLoader(Loader):

    list_name = 'taglines'
    re_guard = 'TAG LINES LIST'

    def iter_taglines(self):
        movie_name = None
        taglines = []

        for line in self.iter_list():
            if line.startswith('# '):
                if movie_name:
                    yield movie_name, taglines
                movie_name = line[2:]
                taglines = []
            elif line:
                taglines.append(line)
        yield movie_name, taglines


    def load(self):
        for idx, (movie_name, taglines) in enumerate(self.iter_taglines()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'taglines': taglines}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print




class ProductionCompaniesLoader(Loader):

    list_name = 'production-companies'
    re_guard = 'PRODUCTION COMPANIES LIST'


    def iter_companies(self):
        for line in self.iter_list():
            data = line.split('\t')
            movie_name, company_name = data[0], data[-1]
            yield movie_name, company_name


    def load(self):
        for idx, (movie_name, company_name) in enumerate(self.iter_companies()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'company_name': company_name}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print




class GenreLoader(Loader):

    list_name = 'genres'
    re_guard = '\d: THE GENRES LIST'


    def iter_genres(self):
        for line in self.iter_list():
            data = line.split('\t')
            movie_name, genre = data[0], data[-1]
            yield movie_name, genre


    def load(self):
        for idx, (movie_name, genre) in enumerate(self.iter_genres()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'genre': genre}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print



class LanguageLoader(Loader):

    list_name = 'language'
    re_guard = 'LANGUAGE LIST'


    def iter_languages(self):
        for line in self.iter_list():
            data = line.split('\t')
            movie_name, language = data[0], data[-1]
            yield movie_name, language


    def load(self):
        for idx, (movie_name, language) in enumerate(self.iter_languages()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'language': language}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print



class CountriesLoader(Loader):

    list_name = 'countries'
    re_guard = 'COUNTRIES LIST'


    def iter_countries(self):
        for line in self.iter_list():
            data = line.split('\t')
            movie_name, country = data[0], data[-1]
            yield movie_name, country


    def load(self):
        for idx, (movie_name, country) in enumerate(self.iter_countries()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'country': country}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print





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
                aka_titles.append(line)
        yield movie_name, aka_titles


    def load(self):
        for idx, (movie_name, aka_titles) in enumerate(self.iter_aka_titles()):

            self.coll_movies.update({'name': movie_name}, {'$push': {'aka_titles': aka_titles}})
            # TODO did the update succeed?

            if not idx % 431: # just a nice prime number
                self.print_progress(idx)

        self.print_total(idx)

        print















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
        ]:
        loader = loader_factory(db=db, plaintext_dir=plaintext_dir)
        loader.load()


