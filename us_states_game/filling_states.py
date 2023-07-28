from turtle import Turtle

class StateFill(Turtle):
    def __init__(self, name: str, coordinates: tuple, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(coordinates)
        self.write(f"{name}")
