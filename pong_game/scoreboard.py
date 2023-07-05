from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, coordinates, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(coordinates)

    def refresh_scoreboard(self):
        self.write(f"{self.score}", move=False,
                   align="center", font=("Arial", 48, "bold"))

    def plus_one(self):
        self.clear()
        self.score += 1
        self.refresh_scoreboard()

    def doesnt_win(self):
        if self.score < 5:
            return True

    def and_the_winner_is(self, name: str, coordinates: tuple):
        if self.score == 5:
            game_over = Scoreboard((coordinates))
            game_over.write(f"{name} won!", move=False,
                            align="center", font=("Arial", 20, "bold"))
