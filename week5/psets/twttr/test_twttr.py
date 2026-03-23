from week5.psets.twttr.twttr import shorten
import pytest


def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("Hello, World") == "Hll, Wrld"

