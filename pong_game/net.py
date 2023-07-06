from turtle import Turtle

Y_EDGES = 290


class Net():
    def __init__(self) -> None:
        self.whole_net()

    def whole_net(self):
        y_edges = Y_EDGES
        while y_edges > - Y_EDGES:
            self.piece_of_net(y_edges)
            y_edges -= 30

    def piece_of_net(self, y_cor: int):
        piece = Turtle("square")
        piece.color("white")
        piece.shapesize(1, 0.2)
        piece.penup()
        piece.goto(0, y_cor)
