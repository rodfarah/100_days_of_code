from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        return self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "bold"))

    def plus_one(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        return self.write("GAME OVER!", False, align="center", font=("Arial", 12, "bold"))
