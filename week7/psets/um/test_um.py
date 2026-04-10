import pytest
from um import count


def test_count():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_count_case_insensitive():
    assert count("um, thanks for the album.") == 1
    assert count("UM, thanks for the album.") == 1
    assert count("uM, thanks for the album.") == 1


def test_count_no_um():
    assert count("Thanks for the album.") == 0
    assert count("Thanks, um...") == 1


def test_count_um_as_part_of_word():
    assert count("Umm, thanks for the album.") == 0
    assert count("Um, thanks for the album.") == 1


def test_count_empty_string():
    assert count("") == 0

