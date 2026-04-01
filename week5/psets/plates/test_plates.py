from plates import is_valid
import pytest

## 1. Maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
## 2. All plates must start with at least two letters.”
## 3. No periods, spaces, or punctuation marks are allowed.
## 4. First number cannot be 0
## 5. Numbers cannot be used in the middle of a plate, only at the end of the plate.

# Recall that a str comes with quite a few methods,
# per docs.python.org/3/library/stdtypes.html#string-methods.


def test_start_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False  # Only one letter
    assert is_valid("1A") == False  # Starts with a number
    assert is_valid("12") == False  # Starts with two numbers


def test_length():
    assert is_valid("a") == False
    assert is_valid("aa") == True
    assert is_valid("aaa") == True
    assert is_valid("aaaa") == True
    assert is_valid("aaaaa") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("aaaaaaa") == False


def test_start_2L():
    assert is_valid("a") == False
    assert is_valid("aa") == True
    assert is_valid("AA") == True
    assert is_valid("1a") == False
    assert is_valid("1aa") == False


def test_alphanum():
    assert is_valid("a!") == False
    assert is_valid("aa!") == False
    assert is_valid("#?.!") == False
    assert is_valid(" spaces ") == False


def test_firstNot0():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("AAAA01") == False
    assert is_valid("AAA01") == False


def test_numbersNotMiddle():
    assert is_valid("AA55AA") == False
    assert is_valid("AA45A") == False


def test_numbersNotBegin():
    assert is_valid("55AAAA") == False
    assert is_valid("45AAA") == False
