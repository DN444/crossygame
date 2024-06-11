STARTING_POSITION = (0, -330)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 330
from turtle import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset()
        self.setheading(90)
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def reset(self):
        self.goto(STARTING_POSITION)
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
