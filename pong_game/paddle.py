from turtle import Turtle

PADDLE_X_POSITION = 360
PADDLE_Y_POSITION = 0


class Paddle(Turtle):
    def __init__(self, side: str, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.side = side
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if self.side == "left":
            self.goto((-PADDLE_X_POSITION, PADDLE_Y_POSITION))
        elif self.side == "right":
            self.goto((PADDLE_X_POSITION, PADDLE_Y_POSITION))

    def go_up(self):
        step_up = self.ycor() + 20
        if self.ycor() <= 220:
            self.goto(self.xcor(), step_up)

    def go_down(self):
        step_up = self.ycor() - 20
        if self.ycor() >= -220:
            self.goto(self.xcor(), step_up)
