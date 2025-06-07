# базовый класс - Фигура
class Shape:
    def area(self):
        # базовая реализация — просто 0
        return 0

# класс Прямоугольник, наследуется от Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        # сохраняем длину и ширину
        self.length = length
        self.width = width

    def area(self):
        # площадь прямоугольника = длина * ширина
        return self.length * self.width

# создаём объект прямоугольника с длиной 4 и шириной 6
rectangle = Rectangle(4, 6)

# выводим площадь
print("Площадь прямоугольника:", rectangle.area())
