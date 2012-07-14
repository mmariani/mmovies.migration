#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Goofs(LoaderBase):
    # XXX refactor, see Trivia

    list_name = 'goofs'
    re_guard = 'GOOFS LIST'

    def consume_goof(self, first_line, it):
        goof_lines = [first_line[2:]]
        while True:
            line = next(it)
            if line:
                goof_lines.append(line[2:])
            else:
                break
        return ' '.join(goof_lines)


    def iter_block(self):
        movie_name = None

        it = self.iter_list()
        while True:
            line = next(it)
            if line.startswith('# '):
                movie_name = line[2:]
            elif line.startswith('- '):
                goof = self.consume_goof(line, it)
                yield movie_name, goof

    def load(self):
        # XXX divide into CHAR, CONT, CREW, FACT, FAIR, FAKE, PLOT, SYNC
        for idx, (movie_name, goof) in enumerate(self.iter_block()):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'goofs': goof}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


