#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.lib.decorators import filter_empty, filter_empty_any
from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class AkaTitles(LoaderBase):

    list_name = 'aka-titles'
    re_guard = 'AKA TITLES LIST'


    @filter_empty_any
    def iter_block(self):
        movie_name = None
        block = []

        for line in self.iter_list():
            if not line.startswith(' '):
                yield movie_name, block
                movie_name, block = line, []
            else:
                block.append(line.strip())
        yield movie_name, block


    @filter_empty
    def parse_block(self, block):
        for line in block:
            yield line


    def load(self):
        for idx, (movie_name, movie_block) in enumerate(self.iter_block()):
            aka_titles = list(self.parse_block(movie_block))
            for aka_title in aka_titles:
                self.coll_movies.update({'name': movie_name}, {'$addToSet': {'aka_titles': aka_title}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


