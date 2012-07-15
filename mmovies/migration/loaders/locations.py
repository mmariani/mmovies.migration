#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Locations(LoaderBase):

    list_name = 'locations'
    re_guard = 'LOCATIONS LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, locations = data[0], data[1].strip()
            yield movie_name, locations

    def load(self):
        for idx, (movie_name, locations) in enumerate(self.iter_line(), 1):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'locations': locations}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


