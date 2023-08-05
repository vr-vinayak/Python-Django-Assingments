import requests
from django.conf import settings

def _movies_search(api_query_params):
    url = f'https://api.themoviedb.org/3/search/movie'

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzJmMDZhM2NmZGEwMDkwNjM1YmY1OWRhM2M0NzdjNiIsInN1YiI6IjY0Y2QyMWYxZjY3ODdhMDBhZjU0YzUxYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yyeuAQEdLP1sdNCnxrvE0TFdravovDXeGtWuGlYaqfs"
    }
    params = {
        'api_key': settings.TMDB_API_KEY,
        **api_query_params
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    return data.get('results', [])