from turtle import Turtle


class Level(Turtle):
    """Higher levels is equal to faster cars."""

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto((-170, 275))
        self.score = 0
        self.increase_level()

    def increase_level(self):
        """Increase level by one"""
        self.score += 1
        self.write(f"Level: {self.score}", align="center",
                   font=("Arial", 16, "bold"))

    def game_over(self):
        """If the car hits the turtle, the game is over"""
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 16, "bold"))
