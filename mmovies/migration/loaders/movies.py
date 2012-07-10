#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Year(LoaderBase):

    list_name = 'movies'
    re_guard = 'MOVIES LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, year = data[0], data[1].strip()
            yield movie_name, year

    def load(self):
        for idx, (movie_name, year) in enumerate(self.iter_line()):
            self.coll_movies.insert({'name': movie_name, 'year': year})
            self.progress(idx)

        self.progress(idx, end=True)


