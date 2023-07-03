from turtle import Turtle

# class Net(Turtle):
#     def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
#         super().__init__(shape, undobuffersize, visible)
#         self.whole_net()

def piece_of_net(coordinates):
    each_block = Turtle("square")
    each_block.speed("fastest")
    each_block.color("white")
    each_block.shapesize(1, 0.2, 1)
    each_block.penup()
    each_block.setposition(coordinates)


def whole_net():
    up_coord = 290
    down_coord = -290
    while up_coord >= down_coord:
        piece_of_net((0, up_coord))
        up_coord -= 30
