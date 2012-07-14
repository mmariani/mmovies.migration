#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from mmovies.migration.loaders import LoaderBase

log = logging.getLogger(__name__)



class MiscellaneousCompanies(LoaderBase):
    # XXX refactor see locations

    list_name = 'miscellaneous-companies'
    re_guard = 'MISCELLANEOUS COMPANY LIST'

    def iter_line(self):
        for line in self.iter_list():
            data = line.split('\t', 1)
            movie_name, companies = data[0], data[1].strip()
            yield movie_name, companies

    def load(self):
        for idx, (movie_name, companies) in enumerate(self.iter_line()):
            self.coll_movies.update({'name': movie_name}, {'$addToSet': {'miscellaneous-companies': companies}})
            self.progress(idx)

        self.progress(idx, end=True)


