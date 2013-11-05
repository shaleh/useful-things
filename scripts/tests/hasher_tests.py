#!/usr/bin/env python

import argparse
from nose.tools import *
import unittest
import sys

import hasher


def test_is_windows_darwin():
    sys.platform = 'darwin'
    assert_false(hasher.is_windows())


def test_is_windows_linux():
    sys.platform = 'linux'
    assert_false(hasher.is_windows())


def test_is_windows():
    sys.platform = 'win32'
    assert_true(hasher.is_windows())


def test_platform_appropriate_parser_darwin():
    sys.platform = 'darwin'

    assert_false(hasher.is_windows())

    parser = hasher.PlatformAppropriateParser(description="Test app")
    parser.add_argument('-f', '--file', dest="file")

    args = parser.parse_args(['-f', 'foo', ])
    assert_equal(args.file, "foo")

    args = parser.parse_args(['--file', 'foo', ])
    assert_equal(args.file, "foo")


def test_platform_appropriate_parser_windows():
    sys.platform = 'win32'

    assert_true(hasher.is_windows())

    parser = hasher.PlatformAppropriateParser(description="Test app")
    parser.add_argument('-f', '--file', dest="file")

    args = parser.parse_args(['/f', 'foo', ])
    assert_equal(args.file, "foo")

    args = parser.parse_args(['/file', 'foo', ])
    assert_equal(args.file, "foo")
