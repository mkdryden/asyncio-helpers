from __future__ import division, print_function, unicode_literals

from asyncio_helpers import with_loop
from nose.tools import eq_
import trollius as asyncio


def test_with_loop():
    @with_loop
    @asyncio.coroutine
    def foo(a):
        raise asyncio.Return(a)

    a = 'hello'
    eq_(foo(a), a)
