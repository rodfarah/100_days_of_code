from turtle import Turtle

class Net(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

    def piece_of_net(self):
        self.color("white")
        self.shape("square")
        self.shapesize(1, 0.2)


    def whole_net(self):
        total_height = 600
        half_height = total_height/2
        while half_height:
            self.goto(-2, half_height)
            self.piece_of_net()
            half_height -= 30
            

