from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-240, 250)
        self.write(arg=f"Level :{self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 250)
        self.write(arg=f"Level :{self.level}", align="center", font=FONT)

    def add_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("courier", 40, "normal"))
