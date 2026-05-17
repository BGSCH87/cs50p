# project.py
import requests

API_KEY = "8b986854"

def main():
    # Een kleine test voor in de terminal zodat je snel kunt zien of je API werkt!
    print("--- Test OMDb API ---")
    resultaten = search_movies("Inception")
    if resultaten:
        print(f"Eerste zoekresultaat: {resultaten[0]['Title']} ({resultaten[0]['Year']})")
    
    details = get_movie_details("tt1375666") # IMDb ID van Inception
    if details:
        print(f"Cast: {details.get('Actors')}")


def search_movies(title):
    """Zoekt films op titel voor de Live Search.
    Geeft een lijst van dictionaries terug met Title, Year, Poster en imdbID."""
    if not title or not title.strip():
        return []
        
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={title.strip()}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # OMDb geeft 'Search' terug als er resultaten zijn
        if "Search" in data:
            return data["Search"]
        return []
    except requests.RequestException:
        return []


def get_movie_details(imdb_id):
    """Haalt uitgebreide details op van één specifieke film op basis van IMDb ID."""
    if not imdb_id:
        return None
        
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("Response") == "True":
            return data
        return None
    except requests.RequestException:
        return None


def validate_rating(rating):
    """Controleert of de gegeven rating een geldig getal is tussen 1 en 5."""
    try:
        score = int(rating)
        if 1 <= score <= 5:
            return True
        return False
    except (ValueError, TypeError):
        return False

def filter_by_rating(movies_list, rating):
    """Filtert een lijst met films op basis van een specifieke rating (1 t/m 5).
    Als de rating 0 of ongeldig is, geven we de hele lijst terug."""
    try:
        score = int(rating)
        if score < 1 or score > 5:
            return movies_list
        
        # Filter de lijst: we vergelijken de 'my_rating' kolom uit de database
        return [movie for movie in movies_list if int(movie["my_rating"]) == score]
    except (ValueError, TypeError):
        return movies_list
        
if __name__ == "__main__":
    main()