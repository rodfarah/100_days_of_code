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
    """Instantiate a snake object, first made of 3 squares"""
    def __init__(self) -> None:
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        """Create a 3 squared snake"""
        for s in range(3):
            global INITIAL_XPOS
            global INITIAL_YPOS
            self.add_square((INITIAL_XPOS, INITIAL_YPOS))
            INITIAL_XPOS -= 20

    def snake_crashes(self):
        for square in self.squares:
            square.goto(500, 500)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def add_square(self, coordinates: tuple[int, int]):
        """Add a square to an existing snake"""
        each_square = Turtle("square")
        each_square.color("white")
        each_square.penup()
        each_square.goto(coordinates)
        self.squares.append(each_square)

    def move(self):
        """Give movement to an existing snake"""
        num_of_squares = len(self.squares)
        for n in range(num_of_squares-1, 0, -1):
            base_cordinate = self.squares[n - 1].position()
            self.squares[n].goto(base_cordinate)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        """Turn a snake up, unless it is heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """Turn a snake right, unless it is heading left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Turn a snake down, unless it is heading up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Turn a snake right, unless it is heading left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
