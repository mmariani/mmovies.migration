#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decorator
import logging

from mmovies.migration.lib.decorators import filter_empty, filter_empty_any
from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)




class AlternateVersions(LoaderBase):

    list_name = 'alternate-versions'
    re_guard = 'ALTERNATE VERSIONS LIST'


    @filter_empty_any
    def iter_block(self):
        movie_name = None
        block = []

        for line in self.iter_list():
            if not line:
                continue
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
        for idx, (movie_name, movie_block) in enumerate(self.iter_block()):
            if movie_name is None:
                continue
            alternate_versions = list(self.parse_block(movie_block))
            self.coll_movies.update({'name': movie_name}, {'$push': {'alternate-versions': alternate_versions}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


