# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Certificates
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
certificates.list

2012-07-05

-----------------------------------------------------------------------------

CERTIFICATES LIST
=================
D & D & F: 'Dungeons & Dragons' & 'Futurama' (2008) (V)	UK:U
D III 38 (1939)						Germany:(Banned)	(1945)
D III 38 (1939)						Sweden:Btl
D no shokutaku (1995) (VG)				USA:T
D no shokutaku (1995) (VG)				UK:15
D no shokutaku 2 (1999) (VG)				USA:M
D' Anothers (2005)					Philippines:G
D' Lucky Ones! (2006)					Philippines:G	(MTRCB)
D' Uragons (2002)					Philippines:PG-13
D'Albertville à Kabalo: les mines de charbon de la Lukuga (1917)	Belgium:KT
D'Artagnan et les trois mousquetaires (2005)		USA:R
D'Artagnan et les trois mousquetaires (2005)		Argentina:13
D'Est (1993)						Argentina:Atp
D'Love (2010)						Singapore:M18
D'Ye Ken John Peel? (1935)				USA:Approved
D'Ye Ken John Peel? (1935)				USA:Passed	(National Board of Review)
D'autres mondes (2004)					Brazil:16
D'homme à hommes (1948)					Germany:12	(nf)
D'homme à hommes (1948)					Finland:K-16
D'homme à hommes (1948)					Sweden:15
D'hommes à hommes (1977)				France:X
D'une brousse à l'autre (1998)				France:U
D-Cup Dating Service (1991) (V)				USA:X
D-Cup Discipline (????) (V)				Germany:18
D-Day (2006)						Singapore:PG
D-Day (2006)						South Korea:15
D-Day (2006)						Germany:16
D-Day Revisited (1968)					Finland:K-15	(2009)
D-Day the Sixth of June (1956)				Netherlands:12
D-Day the Sixth of June (1956)				USA:Approved	(certificate #17873)
D-Day the Sixth of June (1956)				Canada:PG	(video rating)
D-Day the Sixth of June (1956)				UK:A	(original rating)
D-Day the Sixth of June (1956)				UK:PG	(tv rating)
D-Day the Sixth of June (1956)				Australia:PG
D-Day the Sixth of June (1956)				Finland:K-16
D-Day the Sixth of June (1956)				Sweden:15
D-Day the Sixth of June (1956)				UK:PG	(video rating) (1988) (1994)
D-Day the Sixth of June (1956)				West Germany:12
Üç maymun (2008)					UK:15
Üç maymun (2008)					Portugal:M/12
Üç maymun (2008)					Hong Kong:III
Üç maymun (2008)					USA:Unrated
Üç maymun (2008)					Brazil:14
Üç maymun (2008)					Sweden:11
Üç maymun (2008)					New Zealand:M
Üç maymun (2008)					Argentina:16
Þetta er ekkert mál (2006)				Iceland:L
Þriðja nafni (2003)					Iceland:L
--------------------------------------------------------------------------------
"""

class TestCertificates(LoaderTest):
    def test_parse(self):
        Certificates(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'certificates': [
                        u'UK:U'
                        ],
                    u'name': u"D & D & F: 'Dungeons & Dragons' & 'Futurama' (2008) (V)"
                    },
                {
                    u'certificates': [
                        u'Germany:(Banned)\t(1945)',
                        u'Sweden:Btl'
                        ],
                    u'name': u'D III 38 (1939)'
                    },
                {
                    u'certificates': [
                        u'USA:T',
                        u'UK:15'
                        ],
                    u'name':
                    u'D no shokutaku (1995) (VG)'
                    },
                {
                    u'certificates': [
                        u'USA:M'
                        ],
                    u'name': u'D no shokutaku 2 (1999) (VG)'
                    },
                {
                    u'certificates': [
                        u'Philippines:G'
                        ],
                    u'name': u"D' Anothers (2005)"
                    },
                {
                    u'certificates': [
                        u'Philippines:G\t(MTRCB)'
                        ],
                    u'name': u"D' Lucky Ones! (2006)"
                    },
                {
                    u'certificates': [
                        u'Philippines:PG-13'
                        ],
                    u'name': u"D' Uragons (2002)"
                    },
                {
                    u'certificates': [
                        u'Belgium:KT'
                        ],
                    u'name': u"D'Albertville \xe0 Kabalo: les mines de charbon de la Lukuga (1917)"
                    },
                {
                    u'certificates': [
                        u'USA:R',
                        u'Argentina:13'
                        ],
                    u'name': u"D'Artagnan et les trois mousquetaires (2005)"
                    },
                {
                    u'certificates': [
                        u'Argentina:Atp'
                        ],
                    u'name': u"D'Est (1993)"
                    },
                {
                    u'certificates': [
                        u'Singapore:M18'
                        ],
                    u'name': u"D'Love (2010)"
                    },
                {
                    u'certificates': [
                        u'USA:Approved',
                        u'USA:Passed\t(National Board of Review)'
                        ],
                    u'name': u"D'Ye Ken John Peel? (1935)"
                    },
                {
                    u'certificates': [
                        u'Brazil:16'
                        ],
                    u'name': u"D'autres mondes (2004)"
                    },
                {
                    u'certificates': [
                        u'Germany:12\t(nf)',
                        u'Finland:K-16',
                        u'Sweden:15'
                        ],
                    u'name': u"D'homme \xe0 hommes (1948)"
                    },
                {
                    u'certificates': [
                        u'France:X'
                        ],
                    u'name': u"D'hommes \xe0 hommes (1977)"
                    },
                {
                    u'certificates': [
                        u'France:U'
                        ],
                    u'name': u"D'une brousse \xe0 l'autre (1998)"
                    },
                {
                    u'certificates': [
                        u'USA:X'
                        ],
                    u'name': u'D-Cup Dating Service (1991) (V)'
                    },
                {
                    u'certificates': [
                        u'Germany:18'
                        ],
                    u'name': u'D-Cup Discipline (????) (V)'
                    },
                {
                    u'certificates': [
                        u'Singapore:PG',
                        u'South Korea:15',
                        u'Germany:16'
                        ],
                    u'name': u'D-Day (2006)'
                    },
                {
                    u'certificates': [
                        u'Finland:K-15\t(2009)'
                        ],
                    u'name': u'D-Day Revisited (1968)'
                    },
                {
                    u'certificates': [
                        u'Netherlands:12',
                        u'USA:Approved\t(certificate #17873)',
                        u'Canada:PG\t(video rating)',
                        u'UK:A\t(original rating)',
                        u'UK:PG\t(tv rating)',
                        u'Australia:PG',
                        u'Finland:K-16',
                        u'Sweden:15',
                        u'UK:PG\t(video rating) (1988) (1994)', u'West Germany:12'
                        ],
                    u'name': u'D-Day the Sixth of June (1956)'
                    },
                {
                    u'certificates': [
                        u'UK:15',
                        u'Portugal:M/12',
                        u'Hong Kong:III',
                        u'USA:Unrated',
                        u'Brazil:14',
                        u'Sweden:11',
                        u'New Zealand:M',
                        u'Argentina:16'
                        ],
                    u'name': u'\xdc\xe7 maymun (2008)'
                    },
                {
                    u'certificates': [
                        u'Iceland:L'
                        ],
                    u'name': u'\xdeetta er ekkert m\xe1l (2006)'
                    },
                {
                    u'certificates': [
                        u'Iceland:L'
                        ],
                    u'name': u'\xderi\xf0ja nafni (2003)'
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


