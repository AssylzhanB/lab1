def average_imdb_by_category(movies, category):
    total = 0
    count = 0
    for movie in movies:
        if movie['category'].lower() == category.lower():
            total += movie['imdb']
            count += 1
    if count == 0:
        return 0  # если фильмов в категории нет
    return total / count

# Пример использования
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
]

print("Средний рейтинг в категории Romance:", average_imdb_by_category(movies, "Romance"))
