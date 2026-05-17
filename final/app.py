# app.py
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
from project import search_movies, get_movie_details, validate_rating, filter_by_rating

app = Flask(__name__)

DB_FILE = "movies.db"

def get_db_connection():
    """Hulpfunctie om veilig verbinding te maken met de SQLite database."""
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row  # Zorgt ervoor dat we kolommen op naam kunnen aanroepen
    return connection


@app.route("/")
def index():
    """De homepage: toont opgeslagen films en verwerkt de rating-filter."""
    # Haal de gekozen filter op uit de URL (bijv. /?filter_rating=5), standaard is "all"
    chosen_filter = request.args.get("filter_rating", "all")
    
    connection = get_db_connection()
    all_movies = connection.execute("SELECT * FROM movies ORDER BY date_watched DESC").fetchall()
    connection.close()
    
    # Gebruik onze functie uit project.py om te filteren als er een specifieke rating is gekozen
    if chosen_filter != "all":
        filtered_movies = filter_by_rating(all_movies, chosen_filter)
    else:
        filtered_movies = all_movies
        
    return render_template("index.html", movies=filtered_movies, current_filter=chosen_filter)


@app.route("/search")
def search_ajax():
    """De route die jouw JavaScript live aanroept tijdens het typen.
    Geeft een JSON-lijst terug met films."""
    query = request.args.get("q", "")
    
    # Pas zoeken vanaf 3 tekens om de API niet te overbelasten
    if len(query) < 3:
        return jsonify([])
        
    results = search_movies(query)
    # We sturen alleen de relevante velden terug naar de voorkant
    return jsonify(results)


@app.route("/movie/<imdb_id>")
def movie_detail(imdb_id):
    """De dynamische detailpagina voor een specifieke film."""
    movie = get_movie_details(imdb_id)
    if not movie:
        return "Film niet gevonden", 404
        
    return render_template("movie.html", movie=movie)


@app.route("/save", methods=["POST"])
def save_movie():
    """Verwerkt het formulier om een film op te slaan met eigen rating en datum."""
    imdb_id = request.form.get("imdb_id")
    title = request.form.get("title")
    year = request.form.get("year")
    runtime = request.form.get("runtime")
    poster = request.form.get("poster")
    my_rating = request.form.get("my_rating")
    
    # GEVRAAGD: Pak de datum die de gebruiker in het formulier heeft ingevuld
    date_watched = request.form.get("date_watched")
    if not date_watched:
        date_watched = datetime.now().strftime("%Y-%m-%d") # Fallback mocht er iets misgaan
    
    if not validate_rating(my_rating):
        return "Ongeldige rating ingevoerd", 400
        
    connection = get_db_connection()
    try:
        connection.execute("""
            INSERT INTO movies (imdb_id, title, year, runtime, poster, my_rating, date_watched)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (imdb_id, title, year, runtime, poster, int(my_rating), date_watched))
        connection.commit()
    except sqlite3.IntegrityError:
        # Als de film al bestaat, updaten we de rating en de nieuwe datum
        connection.execute("""
            UPDATE movies 
            SET my_rating = ?, date_watched = ?
            WHERE imdb_id = ?
        """, (int(my_rating), date_watched, imdb_id))
        connection.commit()
    finally:
        connection.close()
        
    return redirect(url_for("index"))