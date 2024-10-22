# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
import math


class Color:

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):

        self.red: int = 0
        self.green: int = 0
        self.blue: int = 0

        if self.isValidColor(red):
            self.red = red
        else:
            self.red = 0

        if self.isValidColor(green):
            self.green = green
        else:
            self.green = 0

        if self.isValidColor(blue):
            self.blue = blue
        else:
            self.blue = 0

    def getRed(self) -> int:

        return self.red

    def getGreen(self) -> int:

        return self.green

    def getBlue(self) -> int:

        return self.blue

    def setColors(self, newRed: int, newGreen: int, newBlue: int) -> None:

        self.red = newRed
        self.green = newGreen
        self.blue = newBlue

    def getRGB_t(self) -> tuple:

        return self.red, self.green, self.blue

    def getRGB_l(self) -> list[int]:

        return [self.red, self.green, self.blue]

    def isValidColor(self, color: int) -> bool:

        if color > 255 or color < 0:

            return False

        return True


class Figure:

    def __init__(self, colors: Color):

        self.__sides: list[int] = []
        self.sides_count: int = 0
        self.__color: Color = colors
        self.filed: bool = False

    def get_color(self) -> list[int]:

        return self.__color.getRGB_l()

    def __is_valid_color(self, red: int, green: int, blue: int) -> bool:

        if self.__color.isValidColor(red) and self.__color.isValidColor(green) and self.__color.isValidColor(blue):

            return True

        return False

    def set_color(self, newRed: int, newGreen: int, newBlue: int) -> None:

        self.__color.setColors(newRed, newGreen, newBlue)

    def __is_valid_sides(self, sides: list[int]) -> bool:

        if len(set(sides)) == 1 and [isinstance(side, int) for side in sides]:

            return True

        return False

    def get_sides(self) -> list[int]:

        return self.__sides

    def set_sides(self, new_sides: list[int]) -> None:

        if new_sides.__len__() != self.sides_count or not self.__is_valid_sides(new_sides):

            self.__sides[:] = [1] * self.sides_count

            return

        self.__sides = new_sides


class Circle(Figure):

    def __init__(self, color: Color, sides: list[int]):
        super().__init__(color)

        self.sides_count = 1
        self.set_sides(sides)
        self.__radius = sides[0] / (2 * math.pi)

    def get_square(self) -> float:

        return math.pi * self.__radius ** 2


class Triangle(Figure):

    def __init__(self, color: Color, sides: list[int]):
        super().__init__(color)

        self.sides_count = 3
        self.set_sides(sides)

    def get_square(self) -> float:

        p = sum(self.get_sides()) / 2
        return math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(Figure):

    def __init__(self, color: Color, sidesValue: int):
        super().__init__(color)

        self.sides_count = 12
        self.set_sides(sidesValue)

    def set_sides(self, sideValue):

        self._Figure__sides = [sideValue] * self.sides_count

    def get_volume(self) -> float:

        return self.get_sides()[0] ** 3


circle = Circle(Color(5, 4, 565), [10])
print(circle.get_sides())

cube = Cube(Color(0, 1, 4), 9)
print(cube.get_sides())

triangle = Triangle(Color(255, 45, 6), [5, 6, 7, 8])
print(triangle.get_sides())
