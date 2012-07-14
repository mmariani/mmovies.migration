# -*- coding: utf-8 -*-

from mmovies.migration.loaders import AkaTitles
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
aka-titles.list

2012-07-06

-----------------------------------------------------------------------------

AKA TITLES LIST
===============



"$#*! My Dad Says" (2010)
   (aka "Bleep My Dad Says" (2010))	(USA) (alternative title)
   (aka "Shit My Dad Says" (2010))	(USA) (uncensored intended title)

"$40 a Day" (2002)
   (aka "Forty Dollars a Day" (2002))	(USA) (alternative spelling)

"$weepstake$" (1979)
   (aka "La grande lotteria" (1979))	(Italy)
   (aka "Sweepstakes" (1979))

"'t Is maar een spel" (2002)
   (aka "'t Is maar een spel (powered by Chris Van den Durpel)" (2002))	(Belgium: Flemish title) (complete title)

"'t Schaep Met De 5 Pooten" (2006)
   (aka "'t Spaanse Schaep" (2011))	(Netherlands) (third season title)
   (aka "Vrije Schaep Met De 5 Pooten, 't" (2009))	(Netherlands) (second season title)

"'t Zonnetje in huis" (1993) {Toen was geluk nog ver te zoeken (#5.13)}
   (aka "'t Zonnetje in huis" (1993) {Toen was geluk nog ver te zoeken. (#5.13)})

"'Til Death Do Us Part" (2006)
   (aka "John Waters Presents Love You to Death" (2006))	(Australia) (DVD title)
   (aka "Love You to Death" (2006))	(Canada: English title)
   (aka "Love You to Death" (2006))	(International: English title) (imdb display title)
"""

class TestAkaTitles(LoaderTest):
    def test_parse(self):
        AkaTitles(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'name': u'"$#*! My Dad Says" (2010)',
                    u'aka_titles': [
                        [
                            u'(aka "Bleep My Dad Says" (2010))\t(USA) (alternative title)',
                            u'(aka "Shit My Dad Says" (2010))\t(USA) (uncensored intended title)'
                            ]
                        ]
                    },
                {
                    u'name': u'"$40 a Day" (2002)',
                    u'aka_titles': [
                        [
                            u'(aka "Forty Dollars a Day" (2002))\t(USA) (alternative spelling)'
                            ]
                        ]
                    },
                {
                    u'name': u'"$weepstake$" (1979)',
                    u'aka_titles': [
                        [
                            u'(aka "La grande lotteria" (1979))\t(Italy)', u'(aka "Sweepstakes" (1979))'
                            ]
                        ]
                    },
                {
                    u'name': u'"\'t Is maar een spel" (2002)',
                    u'aka_titles': [
                        [
                            u'(aka "\'t Is maar een spel (powered by Chris Van den Durpel)" (2002))\t(Belgium: Flemish title) (complete title)'
                            ]
                        ]
                    },
                {
                    u'name': u'"\'t Schaep Met De 5 Pooten" (2006)',
                    u'aka_titles': [
                        [
                            u'(aka "\'t Spaanse Schaep" (2011))\t(Netherlands) (third season title)',
                            u'(aka "Vrije Schaep Met De 5 Pooten, \'t" (2009))\t(Netherlands) (second season title)'
                            ]
                        ]
                    },
                {
                    u'name': u'"\'t Zonnetje in huis" (1993) {Toen was geluk nog ver te zoeken (#5.13)}',
                    u'aka_titles': [
                        [
                            u'(aka "\'t Zonnetje in huis" (1993) {Toen was geluk nog ver te zoeken. (#5.13)})'
                            ]
                        ]
                    },
                {
                        u'name': u'"\'Til Death Do Us Part" (2006)',
                        u'aka_titles': [
                            [
                                u'(aka "John Waters Presents Love You to Death" (2006))\t(Australia) (DVD title)',
                                u'(aka "Love You to Death" (2006))\t(Canada: English title)',
                                u'(aka "Love You to Death" (2006))\t(International: English title) (imdb display title)'
                                ]
                            ]
                        }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


