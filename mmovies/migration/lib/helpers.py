# -*- coding: utf-8 -*-

import itertools

PROGRESS_TICKER_SIZE = 431
BATCH_SIZE = PROGRESS_TICKER_SIZE*17



# from http://lucentbeing.com/blog/batching-iterables-in-python/
def batches(iterable, batch_size) :
    '''Returns the given iterable split into batches, of size batch_size.'''

    iterable = iter(iterable)

    counter = itertools.count()

    def ticker(key) :
        return next(counter) // batch_size

    for key, group in itertools.groupby(iterable, ticker) :
        yield group

