#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Trivia(LoaderBase):

    list_name = 'trivia'
    re_guard = 'FILM TRIVIA'

    def consume_trivia(self, first_line, it):
        trivia_lines = [first_line[2:]]
        while True:
            line = next(it)
            if line:
                trivia_lines.append(line[2:])
            else:
                break
        return ' '.join(trivia_lines)


    def iter_block(self):
        movie_name = None

        it = self.iter_list()
        while True:
            line = next(it)
            if line.startswith('# '):
                movie_name = line[2:]
            elif line.startswith('- '):
                trivia = self.consume_trivia(line, it)
                yield movie_name, trivia


    def load(self):
        # TODO: separate trivia into separate attributes if they begin with 'EASTER EGG: ' or 'SPOILER: '
        for idx, (movie_name, trivia) in enumerate(self.iter_block()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'trivia': trivia}})
            self.progress(idx)

        self.progress(idx, end=True)


