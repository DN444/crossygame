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
score=Scoreboard()
screen.listen()
screen.onkeypress(tutel.move_up,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for i in car.all_cars:
        if i.distance(tutel)<15:
            game_is_on=False
            score.game_over()
    if tutel.is_at_finish_line():
        tutel.reset()
        car.level_up()
        score.level_up()

screen.exitonclick()