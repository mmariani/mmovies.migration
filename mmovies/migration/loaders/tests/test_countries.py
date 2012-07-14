# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Countries
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
countries.list

2012-07-06

-----------------------------------------------------------------------------

COUNTRIES LIST
==============
Independence War 2: Edge of Chaos (2001) (VG)		UK
Independence for a Day (2003)				Israel
Independence in Sight (2010) (V)			USA
Independence, B'Gosh (1918)				USA
Independence: A Vision for Living (2011) (V)		USA
Independence: Around the Film 'Kedma', a Film by Amos Gitai (2002)	France
Independence: Around the Film 'Kedma', a Film by Amos Gitai (2002)	Japan
Independence: Around the Film 'Kedma', a Film by Amos Gitai (2002)	Israel
Independencia (1997)					Paraguay
Independencia (2009)					France
Independencia (2009)					Philippines
Independencia (2009)					Germany
Independencia (2009)					Netherlands
Independencia (2010)					Spain
Independent (1998)					Germany
Independent America: Rising from Ruins (2009)		USA
Independent America: Rising from Ruins (2009)		Canada
Independent America: The Two-Lane Search for Mom & Pop (2005) (V)	Canada
--------------------------------------------------------------------------------
"""

class TestCountries(LoaderTest):
    def test_parse(self):
        Countries(db=self.db, plaintext=plaintext).load()
        expected = [
                {u'country': [u'UK'], u'name': u'Independence War 2: Edge of Chaos (2001) (VG)'},
                {u'country': [u'Israel'], u'name': u'Independence for a Day (2003)'},
                {u'country': [u'USA'], u'name': u'Independence in Sight (2010) (V)'},
                {u'country': [u'USA'], u'name': u"Independence, B'Gosh (1918)"},
                {u'country': [u'USA'], u'name': u'Independence: A Vision for Living (2011) (V)'},
                {u'country': [u'France', u'Japan', u'Israel'], u'name': u"Independence: Around the Film 'Kedma', a Film by Amos Gitai (2002)"},
                {u'country': [u'Paraguay'], u'name': u'Independencia (1997)'},
                {u'country': [u'France', u'Philippines', u'Germany', u'Netherlands'], u'name': u'Independencia (2009)'},
                {u'country': [u'Spain'], u'name': u'Independencia (2010)'},
                {u'country': [u'Germany'], u'name': u'Independent (1998)'},
                {u'country': [u'USA', u'Canada'], u'name': u'Independent America: Rising from Ruins (2009)'},
                {u'country': [u'Canada'], u'name': u'Independent America: The Two-Lane Search for Mom & Pop (2005) (V)'}
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


