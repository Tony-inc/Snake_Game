from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape="circle")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def grow(self):
        self.add_segment(self.squares[-1].position())

    def move_snake(self):
        for square in range(len(self.squares)-1, 0, -1):
            """the loop stops at the index 0"""
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)