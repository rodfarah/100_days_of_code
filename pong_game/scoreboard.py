from turtle import Turtle


class Scoreboard(Turtle):
    """A scoreboard is made in order to track players score."""
    def __init__(self, coordinates, points, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.points = points
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(coordinates)

    def refresh_scoreboard(self):
        """Updates the scoreboard. Might be useful each time a player scores points."""
        self.write(f"{self.score}", move=False,
                   align="center", font=("Arial", 48, "bold"))

    def plus_one(self):
        """Add one point to scoreboard object."""
        self.clear()
        self.score += 1
        self.refresh_scoreboard()

    def doesnt_win(self):
        """Return True if score is under 5 points"""
        if self.score < self.points:
            return True

    def and_the_winner_is(self, name: str, coordinates: tuple):
        """Game is over once scoreboard reaches a specific number of points"""
        if self.score == self.points:
            game_over = Scoreboard((coordinates), self.points)
            game_over.write(f"{name} won!", move=False,
                            align="center", font=("Arial", 20, "bold"))
