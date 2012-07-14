# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Trivia
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
trivia.list

2012-07-05

-----------------------------------------------------------------------------

FILM TRIVIA
===========

# "24" (2001) {5:00 a.m.-6:00 a.m. (#1.6)}
- The new IT guy is called Milo Pressman (played by Eric Balfour). In
  the movie Stand By Me (1986), also starring Kiefer Sutherland, a
  scrap yard owner appears bearing the same name.

- Up to this point, Fox had been showing repeats of each episode on
  Friday evenings at 9:00 P.M. in an effort to allow viewers to catch
  up on missed programs. Fox decided to stop the re-runs due to bad
  ratings, though they continued to rebroadcast each week's episode on
  their cable outlet, F-X.

- Kiefer Sutherland appeared on The Tonight Show on November 12, and
  forgetfully gave away the entire ending of this episode.


# "24" (2001) {6:00 a.m.-7:00 a.m. (#1.7)}
- Not only does Ira Gaines have remote access to his contact's
  computer inside the CTU, but apparently several "24" staff members
  as well: 'Michael Loceff' (qv)- writer, 'Virgil Williams (II)' (qv)
  - writer, 'Nicole Burke (I)' (qv) - Second assistant director,
  'Todd Wasserman' (qv) - Production Assistant,
  'Tony Pacheco (I)' (qv) - Production Accountant,
  'Jason Savage (III)' (qv) - Assistant Location Manager. Also, none
  of the IP addresses actually exist. In every listing at least one
  octet is greater than 255 (IP octets range from 0-255). This ensures
  people looking for trivia don't actually try to remotely connect to
  existing IPs.

- The billing of executive producers Joel Surnow and Robert Cochran
  and co-executive producer Stephen Hopkins are moved from the closing
  credits back to the beginning of Act I. Credits for co-executive
  producer Howard Gordon, producer Andrea Newman and co-producers
  Michael Loceff and Robin Chamberlin are moved with them.


# "24" (2001) {7:00 a.m.-8:00 a.m. (#1.8)}
- Jack's opening monologue is introduced in this episode - "Right now,
  terrorists are plotting to assassinate a presidential candidate, my
  teenage daughter is missing, and people that I work with may be
  involved in both. I'm Federal Agent Jack Bauer. Today is going to be
  the longest day of my life." It will change over the course of the
  season as Jack's life changes.

- The IP addresses used in the show were made to be over 255 since
  those addresses don't work, much like 555 is the default prefix for
  phone numbers.

- This episode won an Emmy for editing (Chris Willingham) and received
  an additional nomination for dramatic underscore (Sean Callery).

- Jamey's supposed to be receiving messages using her PDA. However,
  you can clearly see "Memo X of 3" above each of the messages,
  showing that they were pre-written onto the PDA.
"""

class TestTrivia(LoaderTest):
    def test_parse(self):
        Trivia(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'trivia': [
                        u'The new IT guy is called Milo Pressman (played by Eric Balfour). In the movie Stand By Me (1986), '
                        u'also starring Kiefer Sutherland, a scrap yard owner appears bearing the same name.',
                        u'Up to this point, Fox had been showing repeats of each episode on Friday evenings at 9:00 P.M. in '
                        u'an effort to allow viewers to catch up on missed programs. Fox decided to stop the re-runs due to '
                        u'bad ratings, though they continued to rebroadcast each week\'s episode on their cable outlet, F-X.',
                        u'Kiefer Sutherland appeared on The Tonight Show on November 12, and forgetfully gave away the entire '
                        u'ending of this episode.'
                        ],
                    u'name': u'"24" (2001) {5:00 a.m.-6:00 a.m. (#1.6)}'
                    },
                {
                    u'trivia': [
                        u'Not only does Ira Gaines have remote access to his contact\'s computer inside the CTU, but apparently '
                        u'several "24" staff members as well: \'Michael Loceff\' (qv)- writer, \'Virgil Williams (II)\' '
                        u'(qv) - writer, \'Nicole Burke (I)\' (qv) - Second assistant director, \'Todd Wasserman\' (qv) - '
                        u'Production Assistant, \'Tony Pacheco (I)\' (qv) - Production Accountant, \'Jason Savage (III)\' (qv) - '
                        u'Assistant Location Manager. Also, none of the IP addresses actually exist. In every listing at least '
                        u'one octet is greater than 255 (IP octets range from 0-255). This ensures people looking for trivia '
                        u'don\'t actually try to remotely connect to existing IPs.',
                        u'The billing of executive producers Joel Surnow and Robert Cochran and co-executive producer Stephen '
                        u'Hopkins are moved from the closing credits back to the beginning of Act I. Credits for co-executive '
                        u'producer Howard Gordon, producer Andrea Newman and co-producers Michael Loceff and Robin Chamberlin '
                        u'are moved with them.'
                        ],
                    u'name': u'"24" (2001) {6:00 a.m.-7:00 a.m. (#1.7)}'
                    },
                {
                    u'trivia': [
                        u'Jack\'s opening monologue is introduced in this episode - "Right now, terrorists are plotting to '
                        u'assassinate a presidential candidate, my teenage daughter is missing, and people that I work with '
                        u'may be involved in both. I\'m Federal Agent Jack Bauer. Today is going to be the longest day of my '
                        u'life." It will change over the course of the season as Jack\'s life changes.',
                        u'The IP addresses used in the show were made to be over 255 since those addresses don\'t work, '
                        u'much like 555 is the default prefix for phone numbers.',
                        u'This episode won an Emmy for editing (Chris Willingham) and received an additional nomination for '
                        u'dramatic underscore (Sean Callery).'
                        ],
                    u'name': u'"24" (2001) {7:00 a.m.-8:00 a.m. (#1.8)}'
                    }
                ]

        self.assertItemsEqual(self.extract_movies(), expected)


