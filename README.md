# asyncio helpers #

Helper functions, etc. for asyncio development

-------------------------------------------------------------------------------

`cancellable`
-------------

Decorator to add `started` event attribute and `cancel()` method.

The `cancel()` method cancels the running coroutine and by raising a
`CancelledError` exception.

### Usage

```python
from asyncio_helpers import cancellable
import trollius as asyncio

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
    future.result()  # raises `asyncio.CancelledError`
```

-------------------------------------------------------------------------------

`with_loop`
-----------

Decorator to run coroutine within an asyncio event loop.

### Windows file I/O support

Uses `asyncio.ProactorEventLoop` on Windows to support file I/O events, e.g.,
serial device events.

If an event loop is already bound to the thread, but is either a) currently
running, or b) *not a `asyncio.ProactorEventLoop` instance*, the wrapped
function is executed in a new thread running a new `asyncio.ProactorEventLoop`
instance.

### Usage

```python
@with_loop
@asyncio.coroutine
def foo(a):
    raise asyncio.Return(a)

a = 'hello'
assert(foo(a) == a)
```

-------------------------------------------------------------------------------

Install
-------

The latest [`asyncio-helpers` release][3] is available as a
[Conda][2] package from the [`sci-bots`][4] channel.

To install `asyncio-helpers` in an **activated Conda environment**, run:

    conda install -c sci-bots -c conda-forge asyncio-helpers

-------------------------------------------------------------------------------

License
-------

This project is licensed under the terms of the [BSD license](/LICENSE.md)

-------------------------------------------------------------------------------

Contributors
------------

 - Christian Fobel ([@sci-bots](https://github.com/sci-bots))


[1]: https://www.arduino.cc/en/Reference/HomePage
[2]: http://www.scons.org/
[3]: https://github.com/sci-bots/asyncio-helpers
