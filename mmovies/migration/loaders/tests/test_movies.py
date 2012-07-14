# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Year
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
movies.list

6 Jul 2012

-----------------------------------------------------------------------------

MOVIES LIST
===========

!Women Art Revolution (2010)				2010
"!Next?" (1994)						1994-1995
"#1 Single" (2006)					2006
"#1 Single" (2006) {Cats and Dogs (#1.4)}		????
"#1 Single" (2006) {Finishing a Chapter (#1.5)}		????
"#1 Single" (2006) {Is the Grass Greener? (#1.1)}	????
"#1 Single" (2006) {Stay (#1.8)}			????
"#1 Single" (2006) {The Rules of Dating (#1.3)}		????
"#1 Single" (2006) {Timing Is Everything (#1.7)}	????
"#1 Single" (2006) {Window Shopping (#1.2)}		????
"#1 Single" (2006) {Wingman (#1.6)}			????
"#ByMySide" (2012)					2012
"#ByMySide" (2012) {Intro: By My Side (#1.1)}		2012
"#Follow" (2011)					2011
"#Follow" (2011) {Pilot (#1.1)}				2011
"#nitTWITS" (2011)					2011
"#nitTWITS" (2011) {A Very Special Wild Turkey Acoustic Christmas (#1.11)}	2011
"#nitTWITS" (2011) {Be Nice & Stay Sober (#1.3)}	2011
"#nitTWITS" (2011) {Chivalry Ain't Dead (#1.1)}		2011
"#nitTWITS" (2011) {Cooking & Killing (#1.13)}		2011
"#nitTWITS" (2011) {Force Quit (#1.5)}			2011
"#nitTWITS" (2011) {Life Alarm (#1.8)}			2011
"#nitTWITS" (2011) {Make Out (#1.6)}			2011
"#nitTWITS" (2011) {Mute for Murder (#1.2)}		2011
--------------------------------------------------------------------------------
"""

class TestMovies(LoaderTest):
    def test_parse(self):
        Year(db=self.db, plaintext=plaintext).load()
        self.assertItemsEqual(self.extract_movies(),
                              [
                                {u'name': u'!Women Art Revolution (2010)', u'year': u'2010'},
                                {u'name': u'"!Next?" (1994)', u'year': u'1994-1995'},
                                {u'name': u'"#1 Single" (2006)', u'year': u'2006'},
                                {u'name': u'"#1 Single" (2006) {Cats and Dogs (#1.4)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Finishing a Chapter (#1.5)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Is the Grass Greener? (#1.1)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Stay (#1.8)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {The Rules of Dating (#1.3)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Timing Is Everything (#1.7)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Window Shopping (#1.2)}', u'year': u'????'},
                                {u'name': u'"#1 Single" (2006) {Wingman (#1.6)}', u'year': u'????'},
                                {u'name': u'"#ByMySide" (2012)', u'year': u'2012'},
                                {u'name': u'"#ByMySide" (2012) {Intro: By My Side (#1.1)}', u'year': u'2012'},
                                {u'name': u'"#Follow" (2011)', u'year': u'2011'},
                                {u'name': u'"#Follow" (2011) {Pilot (#1.1)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011)', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {A Very Special Wild Turkey Acoustic Christmas (#1.11)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Be Nice & Stay Sober (#1.3)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Chivalry Ain\'t Dead (#1.1)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Cooking & Killing (#1.13)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Force Quit (#1.5)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Life Alarm (#1.8)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Make Out (#1.6)}', u'year': u'2011'},
                                {u'name': u'"#nitTWITS" (2011) {Mute for Murder (#1.2)}', u'year': u'2011'},
                                ])


