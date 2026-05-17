# test_project.py
import pytest
from project import validate_rating, search_movies, get_movie_details, filter_by_rating

def test_validate_rating():
    # Test geldige ratings
    assert validate_rating(1) is True
    assert validate_rating(3) is True
    assert validate_rating(5) is True
    assert validate_rating("4") is True  # String die omgezet kan worden naar int
    
    # Test ongeldige ratings
    assert validate_rating(0) is False
    assert validate_rating(6) is False
    assert validate_rating("vijf") is False
    assert validate_rating(None) is False


def test_search_movies_empty():
    # Als we niks invullen, moeten we een lege lijst terugkrijgen (geen crash)
    assert search_movies("") == []
    assert search_movies("   ") == []


def test_get_movie_details_invalid():
    # Een niet-bestaand IMDb ID mag geen crash veroorzaken maar geeft None
    assert get_movie_details("dit_id_bestaat_niet_123") is None
    assert get_movie_details("") is None

def test_filter_by_rating():
    sample_movies = [
        {"title": "Film A", "my_rating": 5},
        {"title": "Film B", "my_rating": 3},
        {"title": "Film C", "my_rating": 5}
    ]
    assert len(filter_by_rating(sample_movies, 5)) == 2
    assert len(filter_by_rating(sample_movies, 3)) == 1
    assert len(filter_by_rating(sample_movies, 0)) == 3  # Geeft alles terug