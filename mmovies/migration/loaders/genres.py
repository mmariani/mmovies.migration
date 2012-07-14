#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Genres(LoaderBase):

    list_name = 'genres'
    re_guard = '\d: THE GENRES LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, genre = data[0], data[1].strip()
            yield movie_name, genre

    def load(self):
        for idx, (movie_name, genre) in enumerate(self.iter_line()):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'genre': genre}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


