#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Distributors(LoaderBase):

    list_name = 'distributors'
    re_guard = 'DISTRIBUTORS LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, distributor_name = data[0], data[1].strip()
            yield movie_name, distributor_name

    def load(self):
        for idx, (movie_name, distributor_name) in enumerate(self.iter_line()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'distributors': distributor_name}})
            self.progress(idx)

        self.progress(idx, end=True)


