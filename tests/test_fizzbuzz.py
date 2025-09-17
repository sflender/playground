import os
import sys

# Ensure the project root is on sys.path so `src` package can be imported when tests run.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.fizzbuzz import fizzbuzz_value, fizzbuzz_sequence


def test_fizzbuzz_value():
    assert fizzbuzz_value(1) == "1"
    assert fizzbuzz_value(3) == "Fizz"
    assert fizzbuzz_value(5) == "Buzz"
    assert fizzbuzz_value(15) == "FizzBuzz"


def test_fizzbuzz_sequence_first_five():
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    assert list(fizzbuzz_sequence(5)) == expected
