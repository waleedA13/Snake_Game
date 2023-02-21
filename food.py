from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("hot pink")
        self.speed("fastest")
        self.up()
        self.refresh()

    def refresh(self):
        """Creates new food every time the snake eats one"""
        x = randrange(-280, 281, 20)
        y = randrange(-280, 281, 20)
        self.setposition(x, y)
