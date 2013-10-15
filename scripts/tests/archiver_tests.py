#!/usr/bin/env python

import argparse
from nose.tools import *
import unittest

import archiver


def data_factory(data, check_func, check_exceptions_func):
    def wrapped():
        for value, expected in data:
            if isinstance(expected, list):
                yield check_func, value, expected
            elif issubclass(expected, Exception):
                yield check_exceptions_func, value, expected
            else:
                assert "Unknown input"
    for test in wrapped():
        test[0](*test[1:])


def check_chunk_string(value, expected):
    assert_equals(archiver.chunk_string(value, 4), expected)

def check_chunk_string_exceptions(value, expected):
    with assert_raises(expected):
        archiver.chunk_string(value, 4)


def test_chunk_string():
    data = (
        ('abcd', []),
        ('abcdefgh', ['abcd', ]),
        ('abcdefghijkl', ['abcd', 'efgh', ]),
        ('abcde', ValueError),
    )

    data_factory(data, check_chunk_string, check_chunk_string_exceptions)


def check_extensions_handler(value, expected):
    assert_equals(archiver.extensions_handler(value), expected)


def check_extensions_handler_exceptions(value, expected):
    with assert_raises(expected):
        archiver.extensions_handler(value)


def test_extensions_handler():
    data = (
        ('j', ['.j', ]),
        ('p,g', ['.p', '.g', ]),
        ('a,b,c', ['.a', '.b', '.c', ]),
        ('.jpg', ['.jpg', ]),
        ('1', argparse.ArgumentTypeError),
    )

    data_factory(data, check_extensions_handler, check_extensions_handler_exceptions)
