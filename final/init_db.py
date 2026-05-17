# init_db.py
import sqlite3

def initialize_database():
    # Dit maakt movies.db aan als het nog niet bestaat en opent de connectie
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()

    # Maak de tabel aan voor jouw opgeslagen films
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            imdb_id TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            year TEXT,
            runtime TEXT,
            poster TEXT,
            my_rating INTEGER,
            date_watched TEXT
        )
    """)

    connection.commit()
    connection.close()
    print("Database succesvol aangemaakt met de 'movies' tabel!")

if __name__ == "__main__":
    initialize_database()