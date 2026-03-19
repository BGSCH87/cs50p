from professor import generate_integer
import pytest

def test_level_1():
    # Run 100 times to be sure!
    for _ in range(100):
        result = generate_integer(1)
        assert 0 <= result <= 9

def test_level_2():
    for _ in range(100):
        result = generate_integer(2)
        assert 10 <= result <= 99

def test_level_3():
    for _ in range(100):
        result = generate_integer(3)
        assert 100 <= result <= 999
        
def test_invalid_level():
    # This checks that your code crashes correctly if given a bad level
    with pytest.raises(ValueError):
        generate_integer(4)