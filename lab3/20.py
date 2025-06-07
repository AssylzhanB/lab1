def average_imdb(movies):
    if len(movies) == 0:  # проверка, что список не пустой
        return 0
    total = 0
    for movie in movies:
        total += movie['imdb']  # суммируем рейтинги
    return total / len(movies)  # делим на количество фильмов

# Пример использования
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
]

print("Средний рейтинг IMDb:", average_imdb(movies))
