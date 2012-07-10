#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import itertools
import os
import re
import sys
import time

import logging

log = logging.getLogger(__name__)


class ParsingError(Exception):
    pass



def forward_stream(stream, re_guard):
    """
    Returns the part of a stream file after the 're_guard' regular expression matches a complete line,
    then skips lines that are blank or composed by '=' characters.
    """

    for rawline in stream:
        if re.match('^%s$' % re_guard, rawline):
            while True:
                first = next(stream)
                if not re.match('(=*|)\n', first):
                    break
            break
    else:
        raise ParsingError("Cannot parse: %s does not contain the line '%s'" % (stream.name, re_guard))

    return itertools.chain([first], stream)





class LoaderBase(object):

    def __init__(self, db, plaintext_dir):
        self.db = db
        self.plaintext_dir = plaintext_dir
        self.coll_movies = self.db['movies']
        self.t0 = time.time()


    def progress(self, n, end=False):
        if end:
            sys.stdout.write('%d... done (%s secs).' % (n, int(time.time()-self.t0)))
        else:
            if n % 431:
                return
            sys.stdout.write('%d' % n)
            sys.stdout.write(chr(8)*len(str(n)))
        sys.stdout.flush()


    def iter_list(self):
        """
        Yields stripped lines from a list of stuff, either gzipped or not (which is slightly faster).
        A line composed of '-' is discarded.
        """
        # XXX better docstring for this one
        try:
            filename = os.path.join(self.plaintext_dir, '%s.list' % self.list_name)
            fin = open(filename, 'rb')
        except IOError:
            filename = os.path.join(self.plaintext_dir, '%s.list.gz' % self.list_name)
            fin = gzip.GzipFile(filename)

        for rawline in forward_stream(fin, self.re_guard):
            line = rawline.rstrip().decode('latin1')
            if not re.match('-+$', line):
                yield line


