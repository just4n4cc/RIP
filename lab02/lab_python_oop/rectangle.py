from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    figure_type = 'Прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, color_par, width_par, height_par):
        self.width = width_par
        self.height = height_par
        self.fcolor = Color()
        self.fcolor.color = color_par

    def calcSquare(self):
        return self.height *self.width

    def __repr__(self) -> str:
        return '{} {} высотой {} шириной {} и площадью {}'.format(Rectangle.get_figure_type(), self.fcolor.color, self.height, self.width, self.calcSquare())
