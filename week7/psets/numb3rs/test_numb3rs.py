from numb3rs import validate
import pytest


def test_length():
    assert validate("192.168.1") == False
    assert validate("192.168.1.256.5") == False
    assert validate("192.168") == False


def test_numbers():
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.0") == True