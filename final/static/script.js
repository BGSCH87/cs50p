// static/script.js
const searchInput = document.getElementById('search-input');
const resultsUl = document.getElementById('search-results');

// Luister naar ELKE toetsaanslag in de zoekbalk
searchInput.addEventListener('input', async function() {
    const query = searchInput.value.trim();

    // Als de tekst te kort is, verberg het resultatenmenu
    if (query.length < 3) {
        resultsUl.innerHTML = '';
        resultsUl.style.display = 'none';
        return;
    }

    try {
        // Maak een achtergrondverzoek (AJAX) naar onze Flask-route /search
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const movies = await response.json();

        // Maak de lijst leeg voor nieuwe resultaten
        resultsUl.innerHTML = '';

        if (movies && movies.length > 0) {
            movies.forEach(movie => {
                const li = document.createElement('li');
                
                // Gebruik een placeholder als de film geen poster heeft
                const posterUrl = movie.Poster !== 'N/A' ? movie.Poster : 'https://via.placeholder.com/40x60?text=No+Image';
                
                // Zorg ervoor dat er geklikt kan worden naar de unieke detailpagina via het imdbID
                li.innerHTML = `
                    <a href="/movie/${movie.imdbID}">
                        <img src="${posterUrl}" alt="${movie.Title}">
                        <div>
                            <strong>${movie.Title}</strong> <br>
                            <span style="font-size: 13px; color: #8899a6;">${movie.Year}</span>
                        </div>
                    </a>
                `;
                resultsUl.appendChild(li);
            });
            resultsUl.style.display = 'block'; // Toon het dropdown menu
        } else {
            resultsUl.innerHTML = '<li style="padding: 10px; color: #8899a6;">Geen films gevonden...</li>';
            resultsUl.style.display = 'block';
        }

    } catch (error) {
        console.error('Fout tijdens live zoeken:', error);
    }
});

// Verberg de lijst als de gebruiker buiten de zoekbalk klikt
document.addEventListener('click', function(e) {
    if (e.target !== searchInput && e.target !== resultsUl) {
        resultsUl.style.display = 'none';
    }
});