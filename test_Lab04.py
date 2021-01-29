
"""
Script for doing some automatic tests for Lab 3
"""

import pytest
import mock

import Lab04


def test_even_num_short_word(capsys):
    inputs = ["8", "egg"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab04.main()
        if Lab04.challenge:
            assert output == "eggeggeggeggeggeggeggegg"
        else:
            assert output == "eggegg"

def test_even_num_long_word(capsys):
    inputs = ["6", "brocolli"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab04.main()
        if Lab04.challenge:
            assert output == "brocollibrocollibrocollibrocollibrocollibrocolli"
        else:
            assert output == "brocollibrocolli"

def test_odd_num_long_word(capsys):
    inputs = ["41", "brocolli"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab04.main()
        assert output == "long"

def test_odd_num_short_word(capsys):
    inputs = ["11", "egg"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab04.main()
        assert output == "short"

def test_odd_num_border_word(capsys):
    inputs = ["13", "house"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab04.main()
        assert output == "short"
