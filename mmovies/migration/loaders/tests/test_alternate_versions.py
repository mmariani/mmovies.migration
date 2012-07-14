# -*- coding: utf-8 -*-

from mmovies.migration.loaders import AlternateVersions
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
     ftp.fu-berlin.de  in  pub/misc/movies/database/tools/w32/

     ftp.sunet.se  in  /pub/tv+movies/imdb/tools/w32/



----------------------------------------------------------------------------

ALTERNATE VERSIONS LIST
=======================


# 0361140
- The version airing on Cartoon Network deletes the series' usual ending
  credits sequence, instead replacing it with a much shorter montage of scenes
  from the series while an English version of the credits scroll by. This was
  done, because of an image, of nudity, and to reduce overall running time for
  advertising reasons.

# "1000 år - En svensk historia" (1980)
- The show was rerun on Swedish television in 1993 and 2001, but then, the six
  20-minute episodes were edited into two one-hour episodes, comprised of three
  original episodes each. This is also the version that has been distributed on
  Swedish DVD in 2007.

# "12 oz. Mouse" (2005)
- The 12 oz. Mouse Volume One DVD presents the entire series (excluding episode
  13, which is featured separately) as a single, continuous movie, with newly
  produced footage to bridge the gaps between episodes.

# "12 oz. Mouse" (2005) {Spider (#1.4)}
- Another version aired immediately after the premiere of this episode. In this
  alternate version, several scenes were shortened to make room for a drum solo
  by Skillet which went on for several minutes.

# "13 Demon Street" (1959)
- Several episodes from this series were edited together with new footage of
  Chaney as Satan to form the feature film Devil's Messenger (1961).

# "21 Jump Street" (1987)
- In the DVD releases by Anchor Bay Entertainment, most of the music is
  replaced with generic music due to licensing issues.
- In its original syndication, the word "Ass" was dubbed "Tail". DVD version
  has done the same.
- In its original broadcast the word "Suck" was dubbed with "Stink" or "Spit".
  Its DVD release has kept this audio track

----------------------------------------------------------------------------

"""

class TestAlternateVersions(LoaderTest):
    def test_parse(self):
        AlternateVersions(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'alternate-versions': [
                        u"The version airing on Cartoon Network deletes the series' usual ending credits sequence, "
                        u"instead replacing it with a much shorter montage of scenes from the series while an English "
                        u"version of the credits scroll by. This was done, because of an image, of nudity, and to reduce "
                        u"overall running time for advertising reasons."
                        ],
                    u'name': u'0361140'
                    },
                {
                    u'alternate-versions': [
                        u'The show was rerun on Swedish television in 1993 and 2001, but then, the six 20-minute episodes '
                        u'were edited into two one-hour episodes, comprised of three original episodes each. This is also '
                        u'the version that has been distributed on Swedish DVD in 2007.'
                        ],
                    u'name': u'"1000 \xe5r - En svensk historia" (1980)'
                    },
                {
                    u'alternate-versions': [
                        u'The 12 oz. Mouse Volume One DVD presents the entire series (excluding episode 13, which is '
                        u'featured separately) as a single, continuous movie, with newly produced footage to bridge '
                        u'the gaps between episodes.'
                        ],
                    u'name': u'"12 oz. Mouse" (2005)'
                    },
                {
                    u'alternate-versions': [
                        u'Another version aired immediately after the premiere of this episode. In this alternate '
                        u'version, several scenes were shortened to make room for a drum solo by Skillet which went '
                        u'on for several minutes.'
                        ],
                    u'name': u'"12 oz. Mouse" (2005) {Spider (#1.4)}'
                    },
                {
                    u'alternate-versions': [
                        u"Several episodes from this series were edited together with new footage of Chaney as Satan "
                        u"to form the feature film Devil's Messenger (1961)."
                        ],
                    u'name': u'"13 Demon Street" (1959)'
                    },
                {
                    u'alternate-versions': [
                        u'In the DVD releases by Anchor Bay Entertainment, most of the music is replaced with '
                        u'generic music due to licensing issues.',
                        u'In its original syndication, the word "Ass" was dubbed "Tail". DVD version has done the same.',
                        u'In its original broadcast the word "Suck" was dubbed with "Stink" or "Spit". Its DVD '
                        u'release has kept this audio track'
                        ],
                    u'name': u'"21 Jump Street" (1987)'
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


