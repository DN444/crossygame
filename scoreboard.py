from turtle import *
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,300)
        self.level=1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="center",font=FONT)
    def level_up(self):
        self.level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)