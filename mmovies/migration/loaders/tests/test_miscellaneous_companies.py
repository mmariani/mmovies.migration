# -*- coding: utf-8 -*-

from mmovies.migration.loaders import MiscellaneousCompanies
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
miscellaneous-companies.list

6 Jul 2012

-------------------------------------------------------------------------------

MISCELLANEOUS COMPANIES LIST
============================
"'Til Death" (2006)					Central Casting [us]	(extras casting)
"'Til Death" (2006)					Chapman/Leonard Studio Equipment [us]	(camera car)
"'Til Death" (2006)					Chapman/Leonard Studio Equipment [us]	(camera dollies)
"'Til Death" (2006)					LCW Props [us]	(set equipment)
"'Til Death" (2006)					MFX [us]	(main title design and compositing)
"'Til Death" (2006)					MFX [us]	(visual effects)
"'Til Death" (2006)					Reel FX Creative Studios [us]	(titles) (as Reel FX [us])
"'Til Death" (2006)					Reel FX Creative Studios [us]	(titles) (opening titles 2007 season)
"'Til Death" (2006)					Sony Pictures Stock Footage [us]	(stock footage)
"'Til Death" (2006)					Star Waggons [us]	(cast trailers)
"Batman" (1992) {It's Never Too Late (#1.6)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {It's Never Too Late (#1.6)}		Spectrum Animation Studio	(animation services)
"Batman" (1992) {Joker's Favor (#1.7)}			Dong Yang Animation [kr]	(animation services)
"Batman" (1992) {Joker's Favor (#1.7)}			Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Joker's Favor (#1.7)}			NOA Animation [kr]	(layout services)
"Batman" (1992) {Joker's Wild (#1.42)}			Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Lock-Up (#3.9)}			Dong Yang Animation [kr]	(animation services)
"Batman" (1992) {Mad as a Hatter (#1.24)}		Akom Production Company [kr]	(animation services)
"Batman" (1992) {Mad as a Hatter (#1.24)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Make 'Em Laugh (#3.7)}			Dong Yang Animation [kr]	(animation services)
"Batman" (1992) {Moon of the Wolf (#1.36)}		Akom Production Company [kr]	(animation services)
"Batman" (1992) {Moon of the Wolf (#1.36)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Mudslide (#2.3)}			Studio Junio [jp]	(animation services)
"Batman" (1992) {Night of the Ninja (#1.28)}		Dong Yang Animation [kr]	(animation services)
"Batman" (1992) {Night of the Ninja (#1.28)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Nothing to Fear (#1.10)}		Dong Yang Animation [kr]	(animation services)
"Batman" (1992) {Nothing to Fear (#1.10)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Off Balance (#1.44)}			Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {Off Balance (#1.44)}			Sunrise [jp]	(animation services)
"Batman" (1992) {On Leather Wings (#1.2)}		Imagineering Sound, The Walt Disney Company [us]	(post-production facilities)
"Batman" (1992) {On Leather Wings (#1.2)}		Spectrum Animation Studio	(animation services)
--------------------------------------------------------------------------------
"""

class TestMiscellaneousCompanies(LoaderTest):
    def test_parse(self):
        MiscellaneousCompanies(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'miscellaneous-companies': [
                        u'Central Casting [us]\t(extras casting)',
                        u'Chapman/Leonard Studio Equipment [us]\t(camera car)',
                        u'Chapman/Leonard Studio Equipment [us]\t(camera dollies)',
                        u'LCW Props [us]\t(set equipment)',
                        u'MFX [us]\t(main title design and compositing)',
                        u'MFX [us]\t(visual effects)',
                        u'Reel FX Creative Studios [us]\t(titles) (as Reel FX [us])',
                        u'Reel FX Creative Studios [us]\t(titles) (opening titles 2007 season)',
                        u'Sony Pictures Stock Footage [us]\t(stock footage)',
                        u'Star Waggons [us]\t(cast trailers)'
                        ],
                    u'name': u'"\'Til Death" (2006)'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)',
                        u'Spectrum Animation Studio\t(animation services)'],
                    u'name': u'"Batman" (1992) {It\'s Never Too Late (#1.6)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Dong Yang Animation [kr]\t(animation services)',
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)',
                        u'NOA Animation [kr]\t(layout services)'
                        ],
                    u'name': u'"Batman" (1992) {Joker\'s Favor (#1.7)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)'
                        ],
                    u'name': u'"Batman" (1992) {Joker\'s Wild (#1.42)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Dong Yang Animation [kr]\t(animation services)'
                        ],
                    u'name': u'"Batman" (1992) {Lock-Up (#3.9)}'},
                {
                    u'miscellaneous-companies': [
                        u'Akom Production Company [kr]\t(animation services)',
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)'
                        ],
                    u'name': u'"Batman" (1992) {Mad as a Hatter (#1.24)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Dong Yang Animation [kr]\t(animation services)'
                        ],
                    u'name': u'"Batman" (1992) {Make \'Em Laugh (#3.7)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Akom Production Company [kr]\t(animation services)',
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)'
                        ],
                    u'name': u'"Batman" (1992) {Moon of the Wolf (#1.36)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Studio Junio [jp]\t(animation services)'
                        ],
                    u'name': u'"Batman" (1992) {Mudslide (#2.3)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Dong Yang Animation [kr]\t(animation services)',
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)'
                        ],
                    u'name': u'"Batman" (1992) {Night of the Ninja (#1.28)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Dong Yang Animation [kr]\t(animation services)',
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)'
                        ],
                    u'name': u'"Batman" (1992) {Nothing to Fear (#1.10)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)',
                        u'Sunrise [jp]\t(animation services)'
                        ],
                    u'name': u'"Batman" (1992) {Off Balance (#1.44)}'
                    },
                {
                    u'miscellaneous-companies': [
                        u'Imagineering Sound, The Walt Disney Company [us]\t(post-production facilities)',
                        u'Spectrum Animation Studio\t(animation services)'
                        ],
                    u'name': u'"Batman" (1992) {On Leather Wings (#1.2)}'
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


