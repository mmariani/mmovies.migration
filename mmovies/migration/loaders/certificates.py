#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Certificates(LoaderBase):

    list_name = 'certificates'
    re_guard = 'CERTIFICATES LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, certificate = data[0], data[1].strip()
            yield movie_name, certificate

    def load(self):
        for idx, (movie_name, certificate) in enumerate(self.iter_line()):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'certificates': certificate}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


