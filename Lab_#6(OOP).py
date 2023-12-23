class Figure():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_volume_fig(self):
        return self.a * self.b * self.c
    
    def __add__(self, other):
        if isinstance(other, Figure):
            return Figure(self.a + other.a, self.b + other.b, self.c + other.c)
        else:
            TypeError("Unsupported operand type for +")

class A_body_with_an_intemal_cavity(Figure):

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d
    
    def get_volume_intemal_cavity(self):
        return  self.get_volume_fig() - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
    
    def __add__(self, other):
        if isinstance(other, A_body_with_an_intemal_cavity):
            return A_body_with_an_intemal_cavity(self.a + other.a, self.b + other.b, self.c + other.c, max(self.d, other.d))
        else:
            TypeError("Unsupported operand type for +") 
            
class ArrayFigure(Figure):

    def __init__(self, a, b, c, k):
        super().__init__(a, b, c)
        self.k = k

    def get_array_fig(self):
        return [self.a * self.b * self.c] * self.k

if __name__ == '__main__':
    
    figure_1 = Figure(1, 2, 3)
    figure_2 = Figure(7, 8, 9)

    print("figure_1 wolume: ", figure_1.get_volume_fig())
    print("figure_2 wolume: ", figure_2.get_volume_fig())

    body_1 = A_body_with_an_intemal_cavity(1, 2, 3, 1)
    body_2 = A_body_with_an_intemal_cavity(7, 8, 9, 2)

    comb_figure = figure_1 + figure_2
    comb_body = body_1 + body_2

    print("Combined Figure: ", comb_figure.get_volume_fig())
    print("Combined Body: ",  comb_body.get_volume_intemal_cavity())
    print("Array Figure : ", ArrayFigure(1,2,3, 3).get_array_fig())
