import io
import sys
from unittest import mock

import os
import sys

# Ensure the project root is on sys.path so `src` package can be imported when tests run.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.next_word_generator import NextWordGenerator


def test_fit_builds_distribution():
    model = NextWordGenerator()
    text = 'hello world hello world hello you'
    model.fit(text)

    assert 'hello' in model.d
    words, probs = model.d['hello']
    assert set(words) == {'world', 'you'}
    assert abs(sum(probs) - 1.0) < 1e-6


def test_predict_prints_choice():
    model = NextWordGenerator()
    text = 'hello world hello world hello you'
    model.fit(text)

    with mock.patch('src.next_word_generator.random.choice', return_value='world'):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            result = model.predict('hello')
        finally:
            sys.stdout = sys_stdout

        output = captured.getvalue().strip()
        assert output == 'world'


def test_predict_unknown_word_returns_empty_and_no_output():
    model = NextWordGenerator()
    text = 'one two three'
    model.fit(text)

    captured = io.StringIO()
    sys_stdout = sys.stdout
    try:
        sys.stdout = captured
        result = model.predict('nonexistent')
    finally:
        sys.stdout = sys_stdout

    output = captured.getvalue().strip()
    assert output == ''
    assert result == []
