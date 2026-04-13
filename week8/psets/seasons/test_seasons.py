import pytest
from seasons import calculate_age, inflect_minutes
from datetime import date

def test_calculate_age():
    # Test 1 year ago (365 days)
    # 365 * 24 * 60 = 525600
    today = date(2024, 1, 1)
    one_year_ago = date(2023, 1, 1)
    assert calculate_age(one_year_ago, today) == 525600

    # Test 2 years ago (730 days)
    # 730 * 24 * 60 = 1051200
    two_years_ago = date(2022, 1, 1)
    assert calculate_age(two_years_ago, today) == 1051200

def test_inflect_minutes():
    # CS50 requirement: No "and" in the string
    assert inflect_minutes(525600) == "five hundred twenty-five thousand, six hundred"
    assert inflect_minutes(1051200) == "one million, fifty-one thousand, two hundred"
    
    # Test a smaller number to ensure andword="" is working
    # Should be "five hundred twenty-five" NOT "five hundred and twenty-five"
    assert inflect_minutes(525) == "five hundred twenty-five"

def test_leap_year():
    # Testing a leap year span (2020 was a leap year)
    # Feb 2020 adds an extra day
    today = date(2021, 1, 1)
    start = date(2020, 1, 1)
    # 366 days * 24 * 60 = 527040
    assert calculate_age(start, today) == 527040