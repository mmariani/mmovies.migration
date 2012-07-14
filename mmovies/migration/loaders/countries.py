#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Countries(LoaderBase):

    list_name = 'countries'
    re_guard = 'COUNTRIES LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            if len(data) == 1:      # missing country, it happens
                continue
            movie_name, country = data[0], data[1].strip()
            yield movie_name, country


    def load(self):
        for idx, (movie_name, country) in enumerate(self.iter_line()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'country': country}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


