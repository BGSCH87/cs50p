from plates import is_valid
import pytest

## 1. Maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
## 2. All plates must start with at least two letters.”
## 3. No periods, spaces, or punctuation marks are allowed.
## 4. First number cannot be 0
## 5. Numbers cannot be used in the middle of a plate, only at the end of the plate.

# Recall that a str comes with quite a few methods, 
# per docs.python.org/3/library/stdtypes.html#string-methods.

def test_length():
    ...

def test_start_2L():
    ...

def test_alphanum():
    ...

def test_firstNot0():
    ...

def test_numbersNotMiddle():
    ...