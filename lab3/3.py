
class Shape:
    def area(self):
        # базовый метод, возвращает 0
        return 0

# класс Квадрат (Square), наследуется от Shape
class Square(Shape):
    def __init__(self, length):
        # сохраняем длину стороны квадрата
        self.length = length

    def area(self):
        # площадь квадрата = сторона * сторона
        return self.length * self.length

# создаём объект класса Shape
shape = Shape()
print("Площадь фигуры (Shape):", shape.area())  # выводит 0

# создаём объект класса Square
square = Square(5)
print("Площадь квадрата (Square):", square.area())  # выводит 25
