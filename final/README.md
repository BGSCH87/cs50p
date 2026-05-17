# CineLog - Film Tracker By:
Username Edx: SchreuderSMC
Github: BGSCH87


#### Video URL: https://youtu.be/LNiR2W3sKAk

## Beschrijving
CineLog is een dynamische webapplicatie gebouwd met Python en Flask waarmee gebruikers hun persoonlijk bekeken films kunnen zoeken, bekijken en loggen in een database. Het project is ontstaan vanuit de frustratie dat interactie in de terminal vaak visueel beperkt is. CineLog brengt de kracht van Python-logica naar een moderne browseromgeving met een responsieve gebruikersinterface.

Met CineLog kunnen gebruikers live zoeken naar films via een integratie met de OMDb API. Zodra een film wordt geselecteerd, haalt de applicatie gedetailleerde informatie op zoals de cast, runtime en IMDb-beoordeling. Gebruikers kunnen de film vervolgens voorzien van een eigen waardering (1 tot 5 sterren) en een specifieke kijkdatum, om deze vervolgens permanent op te slaan in een lokale SQLite-database. Tot slot bevat de homepage een filterfunctionaliteit om de opgeslagen films snel te sorteren op basis van hun score.

## Architectuur en Ontwerpkeuzes

Om te voldoen aan de strikte eisen van CS50P (met name de automatische tests via `check50` en `pytest`), is er gekozen voor een strikte scheiding tussen de **back-end logica** en de **webinterface**. 

Flask-routes zijn inherent lastig te testen met standaard unit tests zonder complexe test-clients te configureren. Daarom is alle kernlogica (data-manipulatie, API-parsing en input-validatie) geïsoleerd in op zichzelf staande Python-functies binnen `project.py`. Deze functies hebben geen weet van Flask en kunnen daardoor feilloos door `pytest` worden gecontroleerd.

### Belangrijke bestanden en mappen:

*   **`project.py`**: Dit is het hart van de back-end. Het bevat de verplichte `main()` functie en de drie kernfuncties die de logica afhandelen:
    *   `search_movies(title)`: Communiceert met de OMDb API en filtert de ruwe JSON-data naar een schone lijst van filmresultaten.
    *   `get_movie_details(imdb_id)`: Haalt de specifieke detailgegevens op van één film op basis van het unieke IMDb ID.
    *   `validate_rating(rating)`: Controleert of de handmatig ingevoerde score van de gebruiker een geldig getal is tussen de 1 en 5, om database-corruptie te voorkomen.
    *   `filter_by_rating(movies_list, rating)`: Filtert een lijst met database-records op basis van de geselecteerde score.
*   **`test_project.py`**: Bevat de unit tests voor de functies in `project.py` om de robuustheid en foutafhandeling (zoals lege zoekopdrachten of ongeldige ID's) te garanderen.
*   **`app.py`**: De Flask-applicatie. Dit bestand fungeert als de 'controller'. Het vangt de HTTP-verzoeken van de gebruiker op, spreekt de functies in `project.py` aan, beheert de SQL-databaseverbindingen en serveert de juiste HTML-templates.
*   **`movies.db`**: Een SQLite-database met een `movies` tabel waarin de unieke IMDb-ID's, titels, posters, persoonlijke ratings en datums worden opgeslagen.
*   **`static/script.js`**: Verzorgt de **Live Search / Autocomplete** functionaliteit. Het luistert naar toetsaanslagen in de zoekbalk en vuurt asynchrone JavaScript-verzoeken (`fetch`) af naar de Flask-back-end zodra er minimaal 3 tekens zijn getypt. Dit voorkomt dat de pagina constant moet herladen tijdens het zoeken.
*   **`templates/`**: Bevat `index.html` (het dashboard met de film-grid en de rating-filter) en `movie.html` (de detailpagina met het log-formulier).

## Installatie en Vereisten

De applicatie maakt gebruik van een aantal externe Python-libraries die zijn gedocumenteerd in `requirements.txt`:
*   `flask` (voor de webomgeving)
*   `requests` (voor het communiceren met de OMDb API)
*   `pytest` (voor het draaien van de unit tests)

### Installatiestappen:
1. Installeer de benodigde pakketten:
   ```bash
   pip install -r requirements.txt