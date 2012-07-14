#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decorator
import logging

log = logging.getLogger(__name__)



def _filter_empty(f, *args, **kw):
    """
    Applies to an iterator (ie. of strings).
    Filter out returned values that are empty.
    """
    for val in f(*args, **kw):
        if val:
            yield val

def filter_empty(f):
    return decorator.decorator(_filter_empty, f)


def _filter_empty_0(f, *args, **kw):
    """
    Applies to an iterator.
    Filter out returned tuples with an empty first item.
    """
    for tup in f(*args, **kw):
        if tup[0]:
            yield tup

def filter_empty_0(f):
    return decorator.decorator(_filter_empty_0, f)



def _filter_empty_any(f, *args, **kw):
    """
    Applies to an iterator.
    Filter out returned tuples with any empty item.
    """
    for tup in f(*args, **kw):
        if all(tup):
            yield tup

def filter_empty_any(f):
    return decorator.decorator(_filter_empty_any, f)


