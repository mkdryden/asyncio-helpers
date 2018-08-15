from __future__ import division, print_function, unicode_literals
from concurrent.futures import ThreadPoolExecutor

from asyncio_helpers import cancellable
from nose.tools import raises, eq_
import trollius as asyncio


def test_cancellable_cancelled():
    @cancellable
    @asyncio.coroutine
    def _cancellable_test(duration_s):
        print('hello, world!')
        yield asyncio.From(asyncio.sleep(1.))
        print('goodbye, world!')


    with ThreadPoolExecutor() as executor:
        future = executor.submit(_cancellable_test, 1.)
        _cancellable_test.started.wait()
        _cancellable_test.cancel()
        raises(asyncio.CancelledError)(future.result)()


def test_cancellable_done():
    @cancellable
    @asyncio.coroutine
    def _cancellable_test(duration_s):
        raise asyncio.Return(duration_s)


    with ThreadPoolExecutor() as executor:
        duration_s = 1.
        future = executor.submit(_cancellable_test, duration_s)
        eq_(duration_s, future.result())
