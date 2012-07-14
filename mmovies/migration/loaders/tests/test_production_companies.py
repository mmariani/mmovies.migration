# -*- coding: utf-8 -*-

from mmovies.migration.loaders import ProductionCompanies
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
production-companies.list

6 Jul 2012

-----------------------------------------------------------------------------

PRODUCTION COMPANIES LIST
=========================
C U at 9 (2005)						Milgrey Finance & Investments [in]
C U at 9 (2005)						Percept Picture Company [in]
C'Ya (2005) (V)						Sweet Chariot Productions [us]
C'era un castello con 40 cani (1990)			Les Films Ariane [fr]
C'era un castello con 40 cani (1990)			Moviestudio
C'era un castello con 40 cani (1990)			Quartz Film
C'era un castello con 40 cani (1990)			Reteitalia [it]
C'era un castello con 40 cani (1990)			Vides Cinematografica [it]
C'era una volta... (1967)				Cinecittà [it]
C'era una volta... (1967)				Compagnia Cinematografica Champion [it]
C'era una volta... (1967)				Les Films Concordia [fr]
C'eravamo tanto amati (1974)				Dean Film [it]	(in collaboration with)
C'eravamo tanto amati (1974)				Delta Film [it]
C'eravamo tanto amati (1974)				La Deantir
C'est beau une ville la nuit (2006)			Canal+ [fr]	(participation)
C'est beau une ville la nuit (2006)			CinéCinéma [fr]	(participation)
C'est beau une ville la nuit (2006)			France 2 Cinéma [fr]	(co-production)
C'est beau une ville la nuit (2006)			Les Films Christy's [fr]	(co-production)
C'est beau une ville la nuit (2006)			Milagro Films [ca]	(co-production) (as Constellation Films International)
C'est beau une ville la nuit (2006)			Téléfilm Canada [ca]	(participation)
C'est ben beau l'amour (1971)				National Film Board of Canada (NFB) [ca]
C'est bon pour la morale (2007)				L'Etna [fr]
C'est bon pour la santé (1975)				Promocinéma [fr]
C'est comme une peine d'amour (1985)			Les Films Cénatos
C'est comme ça (2005)					Cowbell Productions [cr]
C'est complet! (1903)					Pathé Frères [fr]
--------------------------------------------------------------------------------
"""

class TestGenres(LoaderTest):
    def test_parse(self):
        ProductionCompanies(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'company_name': [
                        u'Milgrey Finance & Investments [in]',
                        u'Percept Picture Company [in]'
                        ],
                    u'name': u'C U at 9 (2005)'
                    },
                {
                    u'company_name': [
                        u'Sweet Chariot Productions [us]'
                        ],
                    u'name': u"C'Ya (2005) (V)"
                    },
                {
                    u'company_name': [
                        u'Les Films Ariane [fr]',
                        u'Moviestudio',
                        u'Quartz Film',
                        u'Reteitalia [it]',
                        u'Vides Cinematografica [it]'
                        ],
                    u'name': u"C'era un castello con 40 cani (1990)"
                    },
                {
                    u'company_name': [
                        u'Cinecitt\xe0 [it]',
                        u'Compagnia Cinematografica Champion [it]',
                        u'Les Films Concordia [fr]'
                        ],
                    u'name': u"C'era una volta... (1967)"
                    },
                {
                    u'company_name': [
                        u'Dean Film [it]\t(in collaboration with)',
                        u'Delta Film [it]',
                        u'La Deantir'
                        ],
                    u'name': u"C'eravamo tanto amati (1974)"
                    },
                {
                    u'company_name': [
                        u'Canal+ [fr]\t(participation)',
                        u'Cin\xe9Cin\xe9ma [fr]\t(participation)',
                        u'France 2 Cin\xe9ma [fr]\t(co-production)',
                        u"Les Films Christy's [fr]\t(co-production)",
                        u'Milagro Films [ca]\t(co-production) (as Constellation Films International)',
                        u'T\xe9l\xe9film Canada [ca]\t(participation)'
                        ],
                    u'name': u"C'est beau une ville la nuit (2006)"
                    },
                {
                    u'company_name': [
                        u'National Film Board of Canada (NFB) [ca]'
                        ],
                    u'name': u"C'est ben beau l'amour (1971)"},
                {
                    u'company_name': [
                        u"L'Etna [fr]"
                        ],
                    u'name': u"C'est bon pour la morale (2007)"
                    },
                {
                    u'company_name': [
                        u'Promocin\xe9ma [fr]'
                        ],
                    u'name': u"C'est bon pour la sant\xe9 (1975)"
                    },
                {
                    u'company_name': [
                        u'Les Films C\xe9natos'
                        ],
                    u'name': u"C'est comme une peine d'amour (1985)"
                    },
                {
                    u'company_name': [
                        u'Cowbell Productions [cr]'
                        ],
                    u'name': u"C'est comme \xe7a (2005)"
                    },
                {
                    u'company_name': [
                        u'Path\xe9 Fr\xe8res [fr]'
                        ],
                    u'name': u"C'est complet! (1903)"
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


