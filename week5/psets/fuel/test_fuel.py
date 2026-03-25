import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")  # X > Y case
    with pytest.raises(ValueError):
        convert("-1/4")  # Negative X case
    with pytest.raises(ValueError):
        convert("1/-4")  # Negative Y case
    with pytest.raises(ValueError):
        convert("5/4")  # X > Y case
    with pytest.raises(ValueError):
        convert("cat/dog") # Non-integer case

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"