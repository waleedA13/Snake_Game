from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.starting_snake()
        self.head = self.body[0]

    def starting_snake(self):
        """Sets the starting positions for the snake"""
        for pos in STARTING_POSITIONS:
            self.create_body(pos)

    def create_body(self, position):
        """Creates body parts for the snake"""
        body = Turtle("square")
        body.color("white")
        body.up()
        body.setposition(position)
        self.body.append(body)

    def move_snake(self):
        """Moves the body of the snake towards the head"""
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].setposition(x, y)
        self.head.forward(MOVE)

    def up(self):
        """Changes direction of head to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes direction of head to down"""
        if self.head.heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        """Changes direction of head to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes direction of head to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def new_body(self, speed):
        """Creates a new body for snake for every food eaten"""
        self.create_body((self.body[-1].xcor(), self.body[-1].ycor()))
        return speed - .001

    def reset(self):
        for body_part in self.body:
            body_part.hideturtle()
        self.body.clear()
        self.starting_snake()
        self.head = self.body[0]

