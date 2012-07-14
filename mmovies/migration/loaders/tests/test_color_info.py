# -*- coding: utf-8 -*-

from mmovies.migration.loaders import ColorInfo
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
color-info.list

5 Jul 2012

-----------------------------------------------------------------------------

COLOR INFO LIST
===============
".hack//Roots" (2006) {Unreturner (#1.14)}		Color
".hack//Roots" (2006) {Violation (#1.19)}		Color
".hack//Roots" (2006) {Welcome to 'The World' (#1.1)}	Color
".hack//SIGN" (2002)					Black and White
".hack//SIGN" (2002)					Color
".hack//SIGN" (2002) {Captured (#1.5)}			Color
".hack//SIGN" (2002) {Castle (#1.14)}			Color
"1 Euro TV" (2005)					Color
"1 Girl 5 Gays" (2009)					Color	(HD)
"1 Girl 5 Gays" (2009)					Color
"1 Kadin 1 Erkek" (2008)				Color	(High Definition)
"1 Leicester Square" (2006)				Color
"1 Non Blonde" (2010)					Color
"1 ret og 2 vrang" (1969)				Black and White
"1 ret og 2 vrang" (1969)				Color
"1 to Remember with Brian Kennedy" (2006)		Color
"1 vs 100" (2007)					Color
"1 vs. 100" (2006)					Color
"1 vs. 100" (2006) {(#1.1)}				Color
ö (2012)						Color
--------------------------------------------------------------------------------
"""

class TestColorInfo(LoaderTest):
    def test_parse(self):
        ColorInfo(db=self.db, plaintext=plaintext).load()
        expected = [
                {u'name': u'".hack//Roots" (2006) {Unreturner (#1.14)}', u'color_info': [u'Color']},
                {u'name': u'".hack//Roots" (2006) {Violation (#1.19)}', u'color_info': [u'Color']},
                {u'name': u'".hack//Roots" (2006) {Welcome to \'The World\' (#1.1)}', u'color_info': [u'Color']},
                {u'name': u'".hack//SIGN" (2002)', u'color_info': [u'Black and White', u'Color']},
                {u'name': u'".hack//SIGN" (2002) {Captured (#1.5)}', u'color_info': [u'Color']},
                {u'name': u'".hack//SIGN" (2002) {Castle (#1.14)}', u'color_info': [u'Color']},
                {u'name': u'"1 Euro TV" (2005)', u'color_info': [u'Color']},
                {u'name': u'"1 Girl 5 Gays" (2009)', u'color_info': [u'Color\t(HD)', u'Color']},
                {u'name': u'"1 Kadin 1 Erkek" (2008)', u'color_info': [u'Color\t(High Definition)']},
                {u'name': u'"1 Leicester Square" (2006)', u'color_info': [u'Color']},
                {u'name': u'"1 Non Blonde" (2010)', u'color_info': [u'Color']},
                {u'name': u'"1 ret og 2 vrang" (1969)', u'color_info': [u'Black and White', u'Color']},
                {u'name': u'"1 to Remember with Brian Kennedy" (2006)', u'color_info': [u'Color']},
                {u'name': u'"1 vs 100" (2007)', u'color_info': [u'Color']},
                {u'name': u'"1 vs. 100" (2006)', u'color_info': [u'Color']},
                {u'name': u'"1 vs. 100" (2006) {(#1.1)}', u'color_info': [u'Color']},
                {u'name': u'\xf6 (2012)', u'color_info': [u'Color']}
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


