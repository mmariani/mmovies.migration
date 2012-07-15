#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class ColorInfo(LoaderBase):

    list_name = 'color-info'
    re_guard = 'COLOR INFO LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, color_info = data[0], data[1].strip()
            yield movie_name, color_info

    def load(self):
        for idx, (movie_name, color_info) in enumerate(self.iter_line(), 1):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'color_info': color_info}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


