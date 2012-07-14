#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import gzip
import itertools
import io
import os
import re
import time

import logging

from mmovies.migration.lib.decorators import filter_empty


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
        raise ParsingError("Cannot parse: data does not contain the line '%s'" % re_guard)

    return itertools.chain([first], stream)





class LoaderBase(object):

    list_name = None
    re_guard = None


    def __init__(self, db, plaintext=None, plaintext_dir=None, encoding='latin1', fprog=None):
        self.db = db
        self.plaintext = plaintext
        self.plaintext_dir = plaintext_dir
        self.coll_movies = self.db['movies']
        self.t0 = time.time()
        self.encoding = encoding
        self.fprog = fprog

        if self.fprog:
            fprog.write('loading %s: ' % self.list_name)


    def progress(self, n, end=False):
        if not self.fprog:
            return

        if not end and n % 431:
            return

        self.fprog.write('%d' % n)

        if end:
            elapsed = time.time()-self.t0
            self.fprog.write(' (%s secs - %d/s).\n' % (int(elapsed), n/elapsed))
        else:
            self.fprog.write(chr(8)*len(str(n)))

        self.fprog.flush()


    @filter_empty
    def iter_list(self):
        """
        Yields stripped lines from a list of stuff, either gzipped or not (which is slightly faster).
        A line composed of '-' is discarded.
        """
        # XXX better docstring for this one

        if self.plaintext:
            fin = io.StringIO(self.plaintext)
        else:
            try:
                filename = os.path.join(self.plaintext_dir, '%s.list' % self.list_name)
                fin = io.open(filename, encoding=self.encoding)
            except IOError:
                filename = os.path.join(self.plaintext_dir, '%s.list.gz' % self.list_name)
                fin_raw = gzip.GzipFile(filename)
                fin = codecs.getreader(self.encoding)(fin_raw)

        for rawline in forward_stream(fin, self.re_guard):
            line = rawline.rstrip()
            if not re.match('-+$', line):
                yield line


