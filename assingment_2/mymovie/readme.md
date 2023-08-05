Sure, here is the README.md file based on the utils, views, urls, and settings.py files you provided:


# MyMovie

A simple Django REST API that allows you to search for movies on The Movie Database (TMDB) and add ratings to them.

## Getting Started

1. Install the dependencies:


pip install -r requirements.txt
```

2. add `TMDB_API_KEY` in settings.py file and add the following variable:

```
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

3. Run the development server:

```
python manage.py runserver


## Usage

The API can be accessed at `http://localhost:8000/`.

### Searching for Movies

You can search for movies by title, year, or genre. For example, to search for movies with the title "The Shawshank Redemption", you would use the following URL:


curl --location 'http://127.0.0.1:8000/movie/movies/movie-search?year=2020&release_date=2020-08-26&title=Ayumi' \
--data ''```

The response will be a JSON object with a list of movies that match your search criteria.

### Adding Movie Ratings

You can add ratings to movies by sending a POST request to the following URL:

```
http://127.0.0.1:8000/movie/movies/add-movie-rating/

The request body must contain the following data:

* `title`: The title of the movie.
* `rating`: The rating for the movie (an integer from 0 to 5).

For example, to add a rating of 4 to the movie "The Shawshank Redemption", you would send the following request:

curl --location 'http://127.0.0.1:8000/movie/movies/add-movie-rating/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "The terminal",
    "rating": 5
}'
```

The response will be a JSON object with a message confirming that the rating was added successfully.

## More Information

For more information, please see the [README.md](README.md) file in the project root directory.
```

I hope this is helpful! Let me know if you have any other questions.