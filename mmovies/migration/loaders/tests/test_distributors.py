# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Distributors
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
distributors.list

6 Jul 2012

-----------------------------------------------------------------------------

DISTRIBUTORS LIST
=================
"!Next?" (1994)						Radiotelevisione Italiana (RAI) [it]	(1994) (worldwide) (TV)
"#1 Single" (2006)					E! Entertainment Television [us]	(2006) (USA) (TV)
"#1 Single" (2006)					E! Entertainment Television [us]	(2006) (worldwide) (TV)
"#ByMySide" (2012)					YouTube [us]	(2012) (worldwide) (all media)
"$#*! My Dad Says" (2010)				5* [gb]	(2011) (UK) (TV)
"$#*! My Dad Says" (2010)				Canadian Television (CTV) [ca]	(2010-2011) (Canada) (TV)
"$#*! My Dad Says" (2010)				Columbia Broadcasting System (CBS) [us]	(2010-2011) (USA) (TV)
"$#*! My Dad Says" (2010)				Nine Network Australia [au]	(2011) (Australia) (TV)
"$#*! My Dad Says" (2010)				Veronica [nl]	(2011) (Netherlands) (TV)
"$#*! My Dad Says" (2010)				Warner Channel Latin America [br]	(2011) (Brazil) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		5* [gb]	(2011) (UK) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		Canadian Television (CTV) [ca]	(2010) (Canada) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		Columbia Broadcasting System (CBS) [us]	(2010) (USA) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		Nine Network Australia [au]	(2011) (Australia) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		Veronica [nl]	(2011) (Netherlands) (TV)
"$#*! My Dad Says" (2010) {Code Ed (#1.4)}		Warner Channel Latin America [br]	(2011) (Brazil) (TV)
"$#*! My Dad Says" (2010) {Corn Star (#1.14)}		5* [gb]	(2011) (UK) (TV)
"$#*! My Dad Says" (2010) {Corn Star (#1.14)}		Canadian Television (CTV) [ca]	(2011) (Canada) (TV)
"$#*! My Dad Says" (2010) {Corn Star (#1.14)}		Columbia Broadcasting System (CBS) [us]	(2011) (USA) (TV)
"$#*! My Dad Says" (2010) {Corn Star (#1.14)}		Veronica [nl]	(2011) (Netherlands) (TV)
--------------------------------------------------------------------------------
"""

class TestDistributors(LoaderTest):
    def test_parse(self):
        Distributors(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'name': u'"!Next?" (1994)',
                    u'distributors': [
                        u'Radiotelevisione Italiana (RAI) [it]'
                        u'\t(1994) (worldwide) (TV)'
                        ]
                    },
                {
                    u'name': u'"#1 Single" (2006)', u'distributors': [
                        u'E! Entertainment Television [us]'
                        u'\t(2006) (USA) (TV)', u'E! Entertainment Television [us]'
                        u'\t(2006) (worldwide) (TV)'
                        ]
                    },
                {u'name': u'"#ByMySide" (2012)',
                    u'distributors': [
                        u'YouTube [us]\t(2012) (worldwide) (all media)'
                        ]
                    },
                {
                    u'name': u'"$#*! My Dad Says" (2010)',
                    u'distributors': [
                        u'5* [gb]'
                        u'\t(2011) (UK) (TV)', u'Canadian Television (CTV) [ca]'
                        u'\t(2010-2011) (Canada) (TV)', u'Columbia Broadcasting System (CBS) [us]'
                        u'\t(2010-2011) (USA) (TV)', u'Nine Network Australia [au]'
                        u'\t(2011) (Australia) (TV)', u'Veronica [nl]'
                        u'\t(2011) (Netherlands) (TV)', u'Warner Channel Latin America [br]'
                        u'\t(2011) (Brazil) (TV)']
                    },
                {
                    u'name': u'"$#*! My Dad Says" (2010) {Code Ed (#1.4)}',
                    u'distributors': [
                        u'5* [gb]'
                        u'\t(2011) (UK) (TV)',
                        u'Canadian Television (CTV) [ca]'
                        u'\t(2010) (Canada) (TV)',
                        u'Columbia Broadcasting System (CBS) [us]'
                        u'\t(2010) (USA) (TV)',
                        u'Nine Network Australia [au]'
                        u'\t(2011) (Australia) (TV)',
                        u'Veronica [nl]'
                        u'\t(2011) (Netherlands) (TV)',
                        u'Warner Channel Latin America [br]'
                        u'\t(2011) (Brazil) (TV)'
                        ]
                    },
                {
                    u'name': u'"$#*! My Dad Says" (2010) {Corn Star (#1.14)}',
                    u'distributors': [
                        u'5* [gb]'
                        u'\t(2011) (UK) (TV)',
                        u'Canadian Television (CTV) [ca]'
                        u'\t(2011) (Canada) (TV)',
                        u'Columbia Broadcasting System (CBS) [us]'
                        u'\t(2011) (USA) (TV)',
                        u'Veronica [nl]'
                        u'\t(2011) (Netherlands) (TV)'
                        ]
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


