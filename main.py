import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=700,height=700)
screen.title("Turtle Crossing Game")
screen.bgcolor("grey")
screen.tracer(0)
tutel=Player()
car=CarManager()
screen.listen()
screen.onkeypress(tutel.move_up,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for i in car.all_cars:
        if i.distance(tutel)<20:
            game_is_on=False
            score=Scoreboard()
            score.game_over()
