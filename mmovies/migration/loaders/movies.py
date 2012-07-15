#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.lib.helpers import batches, BATCH_SIZE
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
        idx = 0
        for batch in batches(self.iter_line(), BATCH_SIZE):
            self.progress(idx)
            insdata = [{'name': movie_name, 'year': year} for movie_name, year in batch]
            idx += len(insdata)
            self.coll_movies.insert(insdata)

        self.progress(idx, end=True)

