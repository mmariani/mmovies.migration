# -*- coding: utf-8 -*-

import unittest

import pymongo


HOST, PORT = '127.0.0.1', 27017


class LoaderTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        conn = pymongo.Connection(HOST, PORT)
        self.db = conn['imdb_testing']
        self.db.drop_collection('movies')


    def iter_movies(self):
        """
        Iterates through loaded data,
        returns the documents without primary key
        for testing purposes.
        """
        for movie in self.db.movies.find({}):
            del movie['_id']
            yield movie


    def extract_movies(self):
        return list(self.iter_movies())


