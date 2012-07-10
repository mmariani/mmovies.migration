#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Plot(LoaderBase):

    list_name = 'plot'
    re_guard = 'PLOT SUMMARIES LIST'

    def iter_block(self):
        movie_name = None
        plot_lines = []

        for line in self.iter_list():
            if line.startswith('MV: '):
                movie_name = line[4:]
                plot_lines = []
            elif line.startswith('PL: '):
                plot_lines.append(line[4:])
            elif line.startswith('BY: '):
                yield movie_name, ' '.join(plot_lines), line[4:]

    def load(self):
        for idx, (movie_name, plot, by) in enumerate(self.iter_block()):
            self.coll_movies.update({'name': movie_name}, {'$push': {'plot': {'text': plot, 'by': by}}})
            self.progress(idx)

        self.progress(idx, end=True)


