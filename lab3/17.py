def is_good_movie(movie):
    return movie['imdb'] > 5.5

# Пример использования
movie_example = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}

print(is_good_movie(movie_example))  # True
