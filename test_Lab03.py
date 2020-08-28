
"""
Script for doing some automatic tests for Lab 3
"""

import pytest
import mock

import Lab03


def test_even_num_short_word(capsys):
    inputs = ["8", "egg"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab03.main()
        assert output == "eggegg"

def test_even_num_long_word(capsys):
    inputs = ["42", "brocolli"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab03.main()
        assert output == "brocollibrocolli"

def test_odd_num_long_word(capsys):
    inputs = ["41", "brocolli"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab03.main()
        assert output == "long"

def test_odd_num_short_word(capsys):
    inputs = ["11", "egg"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab03.main()
        assert output == "short"

def test_odd_num_border_word(capsys):
    inputs = ["13", "house"]
    with mock.patch('builtins.input', side_effect=inputs):
        output = Lab03.main()
        assert output == "short"
