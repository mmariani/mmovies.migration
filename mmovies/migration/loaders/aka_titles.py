#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class AkaTitles(LoaderBase):

    list_name = 'aka-titles'
    re_guard = 'AKA TITLES LIST'

    def iter_block(self):
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
        for idx, (movie_name, aka_titles) in enumerate(self.iter_block()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'aka_titles': aka_titles}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


