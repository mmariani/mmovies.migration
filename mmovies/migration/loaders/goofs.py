#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.lib.decorators import filter_empty, filter_empty_any
from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Goofs(LoaderBase):

    list_name = 'goofs'
    re_guard = 'GOOFS LIST'


    @filter_empty_any
    def iter_block(self):
        movie_name = None
        block = []

        for line in self.iter_list():
            if line.startswith('# '):
                yield movie_name, block
                movie_name, block = line[2:], []
            else:
                block.append(line)
        yield movie_name, block


    @filter_empty
    def parse_block(self, block):
        blocklet = []

        for line in block:
            if line.startswith('- '):
                yield ' '.join(blocklet)
                blocklet = []
            blocklet.append(line[2:])
        yield ' '.join(blocklet)


    def load(self):
        # XXX divide into CHAR, CONT, CREW, FACT, FAIR, FAKE, PLOT, SYNC
        for idx, (movie_name, movie_block) in enumerate(self.iter_block(), 1):
            goofs = list(self.parse_block(movie_block))
            self.coll_movies.update({'name': movie_name}, {'$set': {'goofs': goofs}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


