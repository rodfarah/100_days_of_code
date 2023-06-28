from turtle import Turtle

MOVE_DISTANCE = 20
SPEED = 0.1
INITIAL_XPOS = 0
INITIAL_YPOS = 0
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self) -> None:
        self.squares = []
        self.coordinates = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for s in range(3):
            each_square = Turtle("square")
            each_square.color("white")
            each_square.penup()
            global INITIAL_XPOS
            global INITIAL_YPOS
            each_square.goto(x=INITIAL_XPOS, y=INITIAL_YPOS)
            self.squares.append(each_square)
            self.coordinates.append(each_square.position())
            INITIAL_XPOS -= 20
        # print(self.coordinates)
            
    
    def increase_snake(self):
        ...

    def move(self):
        num_of_squares = len(self.squares)
        for n in range(num_of_squares-1, 0, -1):
            base_cordinate = self.squares[n - 1].position()
            self.squares[n].goto(base_cordinate)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

