COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import *
from random import *

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        chance=randint(1,6)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y=randint(-290,300)
            new_car.goto(350,random_y)
            self.all_cars.append(new_car)
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
            
    