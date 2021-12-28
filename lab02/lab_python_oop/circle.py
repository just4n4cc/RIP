from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
from math import pi

class Circle(Figure):
    figure_type = 'Круг'

    @classmethod
    def get_figure_type(cls) -> str:
        return cls.figure_type

    def __init__(self, color_par, radius_par):
        self.radius = radius_par
        self.fcolor = Color()
        self.fcolor.color = color_par

    def calcSquare(self):
        return self.radius *self.radius *pi

    def __repr__(self) -> str:
        return '{} {} радиуса {} и площадью {}'.format(Circle.get_figure_type() ,self.fcolor.color, self.radius, round(self.calcSquare(), 3))
