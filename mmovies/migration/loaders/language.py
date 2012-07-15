#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class Language(LoaderBase):

    list_name = 'language'
    re_guard = 'LANGUAGE LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            if len(data) == 1:      # missing language, it happens
                continue
            movie_name, language = data[0], data[1].strip()
            yield movie_name, language

    def load(self):
        for idx, (movie_name, language) in enumerate(self.iter_line(), 1):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'language': language}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


