# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Locations
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
locations.list

2012-07-06

-----------------------------------------------------------------------------

LOCATIONS LIST
==============
A 001, operazione Giamaica (1965)			Madrid, Spain
A 001, operazione Giamaica (1965)			Rome, Lazio, Italy
A 008, operazione Sterminio (1965)			Cairo, Egypt
A 008, operazione Sterminio (1965)			Zermatt, Kanton Wallis, Switzerland
A 077, sfida ai killers (1966)				Geneva, Canton de Genève, Switzerland
A 077, sfida ai killers (1966)				Morocco
A 1000 Points of Light (2008) (V)			Asbury Park, New Jersey, USA
A 1000 Points of Light (2008) (V)			Cranford, New Jersey, USA
A 1000 Points of Light (2008) (V)			Jersey City, New Jersey, USA
Absolutely Positive (2006)				Amsterdam, Noord-Holland, Netherlands
Absolutely Positive (2006)				Berlage Lyceum Amsterdam, Noord-Holland, Netherlands
Absolutely Positive (2006)				Centraal Station, Amsterdam, Noord-Holland, Netherlands
Absolution (1978)					Ellesmere College, Shropshire, England, UK
Absolution (1978)					England, UK
Absolution (1978)					Pinewood Studios, Iver Heath, Buckinghamshire, England, UK	(studio)
Absolution (2003) (V)					Chicago, Illinois, USA
Absolution (2003) (V)					St. Louis, Missouri, USA
Absolution (2006) (TV)					Hamilton, Ontario, Canada
Absolution (2006/I)					Scarborough, Toronto, Ontario, Canada
Absolution (2006/II)					Tallahassee, Florida, USA
Absolution (2007)					Cologne, North Rhine - Westphalia, Germany
Absolution (2007)					Düsseldorf, North Rhine - Westphalia, Germany
Absolution (2007) (V)					Vancouver, British Columbia, Canada
--------------------------------------------------------------------------------
"""

class TestGenres(LoaderTest):
    def test_parse(self):
        Locations(db=self.db, plaintext=plaintext).load()
        expected = [
                {u'locations': [u'Madrid, Spain', u'Rome, Lazio, Italy'], u'name': u'A 001, operazione Giamaica (1965)'},
                {u'locations': [u'Cairo, Egypt', u'Zermatt, Kanton Wallis, Switzerland'], u'name': u'A 008, operazione Sterminio (1965)'},
                {u'locations': [u'Geneva, Canton de Gen\xe8ve, Switzerland', u'Morocco'], u'name': u'A 077, sfida ai killers (1966)'},
                {u'locations': [u'Asbury Park, New Jersey, USA', u'Cranford, New Jersey, USA', u'Jersey City, New Jersey, USA'], u'name': u'A 1000 Points of Light (2008) (V)'},
                {u'locations': [u'Amsterdam, Noord-Holland, Netherlands', u'Berlage Lyceum Amsterdam, Noord-Holland, Netherlands', u'Centraal Station, Amsterdam, Noord-Holland, Netherlands'], u'name': u'Absolutely Positive (2006)'},
                {u'locations': [u'Ellesmere College, Shropshire, England, UK', u'England, UK', u'Pinewood Studios, Iver Heath, Buckinghamshire, England, UK\t(studio)'], u'name': u'Absolution (1978)'},
                {u'locations': [u'Chicago, Illinois, USA', u'St. Louis, Missouri, USA'], u'name': u'Absolution (2003) (V)'},
                {u'locations': [u'Hamilton, Ontario, Canada'], u'name': u'Absolution (2006) (TV)'},
                {u'locations': [u'Scarborough, Toronto, Ontario, Canada'], u'name': u'Absolution (2006/I)'},
                {u'locations': [u'Tallahassee, Florida, USA'], u'name': u'Absolution (2006/II)'},
                {u'locations': [u'Cologne, North Rhine - Westphalia, Germany', u'D\xfcsseldorf, North Rhine - Westphalia, Germany'], u'name': u'Absolution (2007)'},
                {u'locations': [u'Vancouver, British Columbia, Canada'], u'name': u'Absolution (2007) (V)'}
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


