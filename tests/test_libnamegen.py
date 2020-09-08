#!/usr/bin/env python3
"""
tests/test_libnamegen.py

Use pytest to test the libnamegen library.
"""

import libnamegen


def test_classic_gen():
    cn = libnamegen.classic.gen()
    assert type(cn) == list
    assert type(cn[0]) == str


def test_random_gen():
    rn = libnamegen.random.gen()
    assert type(rn) == list
    assert type(rn[0]) == str
