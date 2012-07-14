#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Taglines(LoaderBase):

    list_name = 'taglines'
    re_guard = 'TAG LINES LIST'

    def iter_block(self):
        movie_name = None

        for line in self.iter_list():
            if line.startswith('# '):
                movie_name = line[2:]
            elif line:
                yield movie_name, line.strip()

    def load(self):
        for idx, (movie_name, taglines) in enumerate(self.iter_block()):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'taglines': taglines}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


