#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class ProductionCompanies(LoaderBase):

    list_name = 'production-companies'
    re_guard = 'PRODUCTION COMPANIES LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, company_name = data[0], data[1].strip()
            yield movie_name, company_name

    def load(self):
        for idx, (movie_name, company_name) in enumerate(self.iter_line(), 1):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'company_name': company_name}}, True)
            self.progress(idx)

        self.progress(idx, end=True)


