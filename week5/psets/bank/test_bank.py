from bank import value
import pytest

@pytest.mark.parametrize("greeting, expected", [
    ("hello", 0),("Hello", 0),
    ("hey", 20),("Hey", 20),("Hi", 20),
    ("whats up", 100),("Whats up", 100),("Goodday!", 100)
])
def test_multiple_greetings(greeting, expected):
    assert value(greeting) == expected

def test_value_is_integer():
    assert type(value("Hello")) is int
    assert type(value("123456789")) is int
    assert type(value("Hey")) is int
    assert type(value("Whats up")) is int
    assert type(value("")) is int
    assert type(value("!")) is int
    assert type(value("  spaces  ")) is int