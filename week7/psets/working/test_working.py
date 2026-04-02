import pytest
from working import convert

def test_valid_times():
    # Test cases that should work perfectly
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid_hours():
    # Times that are logically impossible
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")

def test_invalid_minutes():
    # Minutes that are out of bounds
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")

def test_invalid_format():
    # Wrong words or missing parts
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM") # Using a dash instead of 'to'
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM") # Missing the word 'to'
    with pytest.raises(ValueError):
        convert("9 to 5") # Missing AM/PM