#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pymongo

from mmovies.migration import loaders

import logging

log = logging.getLogger(__name__)



HOST, PORT = '127.0.0.1', 27017

# XXX look for tabs within imported fields - they might need to be split further




def main(plaintext_dir):
    conn = pymongo.Connection(HOST, PORT)

    db = conn['imdb']

    # purge the old data before loading
    db.drop_collection('movies')

    coll_movies = db['movies']
    coll_movies.create_index([("name", pymongo.ASCENDING)])

    for loader_factory in [
            loaders.Year,
            loaders.Taglines,
            loaders.ProductionCompanies,
            loaders.Genres,
            loaders.Language,
            loaders.Countries,
            loaders.AkaTitles,
            loaders.Plot,
            loaders.Trivia,
            loaders.ColorInfo,
            loaders.Goofs,
            loaders.Distributors,
            loaders.MiscellaneousCompanies,
            loaders.Locations,
            loaders.AlternateVersions,
            loaders.Certificates,
        ]:
        loader = loader_factory(db=db, plaintext_dir=plaintext_dir, fprog=sys.stdout)
        loader.load()


