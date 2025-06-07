def good_movies(movies):
    result = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            result.append(movie)
    return result

# Пример использования
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
]

print(good_movies(movies))


