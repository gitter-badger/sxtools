# -*- encoding: utf-8 -*-

from sxtools import cachedef
import unittest
import datetime
import os

foo_executando = False

@cachedef(
    # seed so that the cache be saved alone
    seed='foo',
    # directory cache
    path='/tmp' if os.path.exists('c:/') else 'c:/tmp',
    # cache time in minutes
    minuteexpire=15,
    # debug mode
    debug=False
)
def foo(a, b):
    global foo_executando
    foo_executando = True
    return a + b


class CacheDefTestCase(unittest.TestCase):

    def test_cachedef_1(self):
        self.assertEqual(3, foo(1, 2))
        self.assertEqual(3, foo(1, 2))

    def test_cachedef_2(self):
        global foo_executando
        self.assertEqual(4, foo(1, 3))
        foo_executando = False
        self.assertEqual(4, foo(1, 3))
        self.assertFalse(foo_executando)
        foo_executando = True
        self.assertEqual(4, foo(1, 3, ignore_cache=True))
        self.assertTrue(foo_executando)


if __name__ == '__main__':
    unittest.main()
