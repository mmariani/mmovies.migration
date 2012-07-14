# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Language
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
language.list

2012-07-05

-----------------------------------------------------------------------------

LANGUAGE LIST
=============
Yuuwaku kyoushi maruhi kyonyuu ressun (2009)		Japanese
Yuuyake wa moeteiruka? (2006)				Japanese
Yuva (2004)						Hindi
Yuva (2004)						Bengali
Yuvabharatham (1990)					Telugu
Yuvadharam Bilisindi (1985)				Tamil
Yuvadharam Bilisindi (1985)				Telugu
Yuvajanotsavam (1986)					Malayalam
Yuvakudu (2000)						Telugu
Yuvami yikamazsin (1947)				Turkish
Yuvami yikamazsin (1969)				Turkish
Yuvana dön baba (1968)					Turkish
Yuvanin bekçileri (1977)				Turkish
Yuvaraju (1982)						Telugu
Þetta er ekkert mál (2006)				Icelandic
Þetta er ekkert mál (2006)				English
Þjóðskinna (1973) (TV)					Icelandic
Þriðja nafni (2003)					Icelandic
Þriðja nafni (2003)					English
Þröng sýn (2005)					Icelandic	(no dialogue)
Þyngdarafl (2010)					Icelandic
--------------------------------------------------------------------------------
"""

class TestGenres(LoaderTest):
    def test_parse(self):
        Language(db=self.db, plaintext=plaintext).load()
        expected = [
                {u'name': u'Yuuwaku kyoushi maruhi kyonyuu ressun (2009)', u'language': [u'Japanese']},
                {u'name': u'Yuuyake wa moeteiruka? (2006)', u'language': [u'Japanese']},
                {u'name': u'Yuva (2004)', u'language': [u'Hindi', u'Bengali']},
                {u'name': u'Yuvabharatham (1990)', u'language': [u'Telugu']},
                {u'name': u'Yuvadharam Bilisindi (1985)', u'language': [u'Tamil', u'Telugu']},
                {u'name': u'Yuvajanotsavam (1986)', u'language': [u'Malayalam']},
                {u'name': u'Yuvakudu (2000)', u'language': [u'Telugu']},
                {u'name': u'Yuvami yikamazsin (1947)', u'language': [u'Turkish']},
                {u'name': u'Yuvami yikamazsin (1969)', u'language': [u'Turkish']},
                {u'name': u'Yuvana d\xf6n baba (1968)', u'language': [u'Turkish']},
                {u'name': u'Yuvanin bek\xe7ileri (1977)', u'language': [u'Turkish']},
                {u'name': u'Yuvaraju (1982)', u'language': [u'Telugu']},
                {u'name': u'\xdeetta er ekkert m\xe1l (2006)', u'language': [u'Icelandic', u'English']},
                {u'name': u'\xdej\xf3\xf0skinna (1973) (TV)', u'language': [u'Icelandic']},
                {u'name': u'\xderi\xf0ja nafni (2003)', u'language': [u'Icelandic', u'English']},
                {u'name': u'\xder\xf6ng s\xfdn (2005)', u'language': [u'Icelandic\t(no dialogue)']},
                {u'name': u'\xdeyngdarafl (2010)', u'language': [u'Icelandic']}
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


