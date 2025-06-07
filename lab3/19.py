def movies_by_category(movies, category):
    result = []
    for movie in movies:
        if movie['category'].lower() == category.lower():
            result.append(movie)
    return result

# Пример использования
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
]

print(movies_by_category(movies, "Romance"))
