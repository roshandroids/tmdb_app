from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TMDB_API_KEY = '1f9d37ed70d3c63a416264a1e0299df0'
TMDB_API_BASE_URL = 'https://api.themoviedb.org/3/'


@app.route('/')
def index():
    # Check if a search query is present in the request
    search_query = request.args.get('search', '')

    if search_query:
        # Fetch search results
        search_results = search_movies(search_query)
        return render_template('index.html', movies=search_results, search_query=search_query)
    else:
        # Fetch popular movies if no search query
        popular_movies = get_popular_movies()
        return render_template('index.html', movies=popular_movies, search_query='')


def get_popular_movies():
    url = f'{TMDB_API_BASE_URL}movie/popular'
    params = {'api_key': TMDB_API_KEY}
    response = requests.get(url, params=params)
    return response.json().get('results', [])


def search_movies(query):
    url = f'{TMDB_API_BASE_URL}search/movie'
    params = {'api_key': TMDB_API_KEY, 'query': query}
    response = requests.get(url, params=params)
    return response.json().get('results', [])


if __name__ == '__main__':
    app.run(debug=True)
