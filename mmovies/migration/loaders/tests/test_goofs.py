# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Goofs
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
goofs.list

2012-07-05

-----------------------------------------------------------------------------

GOOFS LIST
==========

# "'Allo 'Allo!" (1982)
- MISC: At the end of each episode there is a list of "Cast in order
  of appearance", but on several occasions, the order of the list does
  not reflect the actual order in which the actors appear in the
  episode. In season 5, there are even some episodes where actors are
  credited in the list without appearing in the episode.

- FACT: The flag on the helmets of the German soldiers is not a German
  flag. The German flag is yellow-red-black, while the flag on the
  helmet is red-yellow-black.


# "'Til Death" (2006) {Come Out and Play (#2.3)}
- CONT: When Steph and Jeff help Eddie into the kitchen, Steph places
  a bottle of Coke to the left of Eddie. In the next shot, the bottle
  is to his right. Then, the bottle proceeds to move from one side of
  the table to the other in the successive shots.

- CONT: After Eddie opens the bottle of Coke in the kitchen, it fizzes
  up and spills. Then after Steph catches him cleaning it up, the
  bottle goes from having the cap off to having the cap on. Then, once
  Eddie sits back in the chair, the volume of the bottle fluctuates as
  does the location of the bottle cap.
"""

class TestGenres(LoaderTest):
    def test_parse(self):
        Goofs(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'goofs': [
                        u'MISC: At the end of each episode there is a list of "Cast in order of appearance", '
                        u'but on several occasions, the order of the list does not reflect the actual order '
                        u'in which the actors appear in the episode. In season 5, there are even some episodes '
                        u'where actors are credited in the list without appearing in the episode.',
                        u'FACT: The flag on the helmets of the German soldiers is not a German flag. The German '
                        u'flag is yellow-red-black, while the flag on the helmet is red-yellow-black.'
                        ],
                    u'name': u'"\'Allo \'Allo!" (1982)'
                    },
                {
                    u'goofs': [
                        u'CONT: When Steph and Jeff help Eddie into the kitchen, Steph places a bottle of Coke '
                        u'to the left of Eddie. In the next shot, the bottle is to his right. Then, the bottle '
                        u'proceeds to move from one side of the table to the other in the successive shots.'
                        ],
                    u'name': u'"\'Til Death" (2006) {Come Out and Play (#2.3)}'
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


