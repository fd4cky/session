from abc import ABC, abstractmethod


class Shape(ABC):
    """Этот класс определяет общий интерфейс для фигур, которые могут быть нарисованы на холсте."""

    def __init__(self, x, y, color):
        """Args:
            x (int): Координата x.
            y (int): Координата y.
            color (str): Цвет фигуры.
        """
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, canvas):  # canvas на будущее, если реально будут рисоваться фигуры, но сейчас добавлять мне это ЛЕНЬ
        pass


class Circle(Shape):
    """ЭТО КРУГ, наследуется от Shape"""

    def __init__(self, x, y, radius, color):
        """Args:
            x (int): Координата x центра круга.
            y (int): Координата y центра круга.
            radius (int): Радиус круга.
            color (str): Цвет круга.
        """
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, canvas=0):
        """Отрисовывает круг на холсте."""

        print(f"Рисуем круг ({self.x}, {self.y}), с радиусом {self.radius}, "
              f"цвета {self.color}")


class Rectangle(Shape):
    """ПРЯМОУГОЛЬНИК, наследующий от Shape."""

    def __init__(self, x, y, width, height, color):
        """Args:
            x (int): Координата x верхнего левого угла прямоугольника.
            y (int): Координата y верхнего левого угла прямоугольника.
            width (int): Ширина прямоугольника.
            height (int): Высота прямоугольника.
            color (str): Цвет прямоугольника.
        """
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas=0):
        """Отрисовывает прямоугольник"""
        print(f"Рисуем прямоугольник ({self.x}, {self.y}), размер {self.width}x{self.height}, "
              f"цвет {self.color}")


class Line(Shape):
    """ЛИНИЯ, наследующаяся от Shape."""

    def __init__(self, x1, y1, x2, y2, color):
        """
        Примечание: x и y из родительского класса Shape используются как x1 и y1 (начальная точка).

        Args:
            x1 (int): Координата x начальной точки линии.
            y1 (int): Координата y начальной точки линии.
            x2 (int): Координата x конечной точки линии.
            y2 (int): Координата y конечной точки линии.
            color (str): Цвет линии.
        """
        super().__init__(x1, y1, color)  # x и y родительского класса используются как x1 и y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas=0):
        """Отрисовывает линию на холсте."""
        print(f"Рисуем линию от ({self.x}, {self.y}) до ({self.x2}, {self.y2}), "
              f"цвета {self.color}")
