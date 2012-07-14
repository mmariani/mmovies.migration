# -*- coding: utf-8 -*-

from mmovies.migration.loaders import Taglines
from mmovies.migration.loaders.tests.base import LoaderTest


plaintext = u"""
-----------------------------------------------------------------------------

TAG LINES LIST
==============

# "Big Ideas for a Small Planet" (2007)
	Innovators on the leading edge of a new green world.

# "Big Love" (2006)
	Polygamy Loves Company
	Do you think that being married with 3 women is a dream? Think again!

# "Big Love: Inside the Episode" (2011)
	Everything comes to light.

# "Big Morning Buzz Live" (2011)
	Tune in tomorrow morning to see what all the buzz is about!

# "Big Shot Live" (2008)
	Everybody Has A Dream

# "Big Thinkers" (2001)
	Probe Today's Most Brilliant Minds

# "Big Time Rush" (2009) {Live from Times Square (#1.19)}
	This is your all-access pass to the ultimate concert event!

# "Big Top Talent" (1980)
	It's Always Fun Under The Big Top!

# "Big Train" (1998)
	Like reality, only better!

# "Biker Mice from Mars" (2006)
	Let's Rock 'n' Ride!
	In this wild and woolly universe there's only three things you can count on. Your brains... your bros... and your bikes!
	Ride Free, Citizens!
	Let's Rock And Ride!
--------------------------------------------------------------------------------
"""

class TestTaglines(LoaderTest):
    def test_parse(self):
        Taglines(db=self.db, plaintext=plaintext).load()
        expected = [
                {
                    u'taglines': [
                        u'Innovators on the leading edge of a new green world.'
                        ],
                    u'name': u'"Big Ideas for a Small Planet" (2007)'
                    },
                {
                    u'taglines': [
                        u'Polygamy Loves Company',
                        u'Do you think that being married with 3 women is a dream? Think again!'
                        ],
                    u'name': u'"Big Love" (2006)'},
                {
                    u'taglines': [
                        u'Everything comes to light.'
                        ],
                    u'name': u'"Big Love: Inside the Episode" (2011)'
                    },
                {
                    u'taglines': [
                        u'Tune in tomorrow morning to see what all the buzz is about!'
                        ],
                    u'name': u'"Big Morning Buzz Live" (2011)',
                    },
                {
                    u'taglines': [
                        u'Everybody Has A Dream'
                        ],
                    u'name': u'"Big Shot Live" (2008)'
                    },
                {
                    u'taglines': [
                        u"Probe Today's Most Brilliant Minds"
                        ],
                    u'name': u'"Big Thinkers" (2001)'
                    },
                {
                    u'taglines': [
                        u'This is your all-access pass to the ultimate concert event!'
                        ],
                    u'name': u'"Big Time Rush" (2009) {Live from Times Square (#1.19)}'
                    },
                {
                    u'taglines': [
                        u"It's Always Fun Under The Big Top!"
                        ],
                    u'name': u'"Big Top Talent" (1980)'
                    },
                {
                    u'taglines': [
                        u'Like reality, only better!'
                        ],
                    u'name': u'"Big Train" (1998)'
                    },
                {
                    u'taglines': [
                        u"Let's Rock 'n' Ride!",
                        u"In this wild and woolly universe there's only three things you can count on. Your brains... your bros... and your bikes!",
                        u'Ride Free, Citizens!',
                        u"Let's Rock And Ride!"
                        ],
                    u'name': u'"Biker Mice from Mars" (2006)'
                    }
                ]


        self.assertItemsEqual(self.extract_movies(), expected)


