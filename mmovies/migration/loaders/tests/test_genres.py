# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Genres
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""

8: THE GENRES LIST
==================

!Women Art Revolution (2010)				Documentary
"!Next?" (1994)						Documentary
"#1 Single" (2006)					Reality-TV
"#ByMySide" (2012)					Drama
"#Follow" (2011)					Mystery
"#nitTWITS" (2011)					Comedy
"$#*! My Dad Says" (2010)				Comedy
"$1,000,000 Chance of a Lifetime" (1986)		Game-Show
"$100 Makeover" (2010)					Reality-TV
"$100 Taxi Ride" (2001)					Documentary
"$100,000 Name That Tune" (1984)			Game-Show
"$100,000 Name That Tune" (1984)			Music
"$2 Bill" (2002)					Documentary
"$2 Bill" (2002)					Music
"$2 Bill" (2002)					Music
"$2 Bill" (2002)					Music
"$2 Bill" (2002) {Kanye West}				Music
"$25 Million Dollar Hoax" (2004)			Reality-TV
"$40 a Day" (2002)					Documentary
"$5 Cover" (2009)					Drama
"$5 Cover: Seattle" (2009)				Drama
"$50,000 Letterbox" (1980)				Game-Show
"$9.99" (2003)						Adventure
à parte (2010)						Crime
à parte (2010)						Short
à prendre ou à laisser (2010)				Drama
à prendre ou à laisser (2010)				Short
ça promet ! (2011)					Comedy
ça promet ! (2011)					Short
ìCàcaro! (2002)						Short
ìMaten a ese hijo de la chingada! (2008) (V)		Action
íslenska, on the Road to Unearth Iceland's Secrets... (2007)	Adventure
íslenska, on the Road to Unearth Iceland's Secrets... (2007)	Short
ö (2012)						Animation
ö (2012)						Short
"""

class TestGenres(LoaderTest):
    def test_parse(self):
        Genres(db=self.db, plaintext=plaintext).load()
        expected = [
                {u'genre': [u'Documentary'], u'name': u'!Women Art Revolution (2010)'},
                {u'genre': [u'Documentary'], u'name': u'"!Next?" (1994)'},
                {u'genre': [u'Reality-TV'], u'name': u'"#1 Single" (2006)'},
                {u'genre': [u'Drama'], u'name': u'"#ByMySide" (2012)'},
                {u'genre': [u'Mystery'], u'name': u'"#Follow" (2011)'},
                {u'genre': [u'Comedy'], u'name': u'"#nitTWITS" (2011)'},
                {u'genre': [u'Comedy'], u'name': u'"$#*! My Dad Says" (2010)'},
                {u'genre': [u'Game-Show'], u'name': u'"$1,000,000 Chance of a Lifetime" (1986)'},
                {u'genre': [u'Reality-TV'], u'name': u'"$100 Makeover" (2010)'},
                {u'genre': [u'Documentary'], u'name': u'"$100 Taxi Ride" (2001)'},
                {u'genre': [u'Game-Show', u'Music'], u'name': u'"$100,000 Name That Tune" (1984)'},
                {u'genre': [u'Documentary', u'Music'], u'name': u'"$2 Bill" (2002)'},
                {u'genre': [u'Music'], u'name': u'"$2 Bill" (2002) {Kanye West}'},
                {u'genre': [u'Reality-TV'], u'name': u'"$25 Million Dollar Hoax" (2004)'},
                {u'genre': [u'Documentary'], u'name': u'"$40 a Day" (2002)'},
                {u'genre': [u'Drama'], u'name': u'"$5 Cover" (2009)'},
                {u'genre': [u'Drama'], u'name': u'"$5 Cover: Seattle" (2009)'},
                {u'genre': [u'Game-Show'], u'name': u'"$50,000 Letterbox" (1980)'},
                {u'genre': [u'Adventure'], u'name': u'"$9.99" (2003)'},
                {u'genre': [u'Crime', u'Short'], u'name': u'\xe0 parte (2010)'},
                {u'genre': [u'Drama', u'Short'], u'name': u'\xe0 prendre ou \xe0 laisser (2010)'},
                {u'genre': [u'Comedy', u'Short'], u'name': u'\xe7a promet ! (2011)'},
                {u'genre': [u'Short'], u'name': u'\xecC\xe0caro! (2002)'},
                {u'genre': [u'Action'], u'name': u'\xecMaten a ese hijo de la chingada! (2008) (V)'},
                {u'genre': [u'Adventure', u'Short'], u'name': u"\xedslenska, on the Road to Unearth Iceland's Secrets... (2007)"},
                {u'genre': [u'Animation', u'Short'], u'name': u'\xf6 (2012)'}
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


