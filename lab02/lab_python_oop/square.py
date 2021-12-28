from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_type = 'Квадрат'

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, color_par, width_par):
        Rectangle.__init__(self, color_par, width_par, width_par)


    def __repr__(self) -> str:
        return '{} {} высотой {} шириной {} и площадью {}'.format(Square.get_figure_type(), self.fcolor.color, self.height, self.width, self.calcSquare())
