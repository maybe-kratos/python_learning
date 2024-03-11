from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 270:
            return True
        else:
            return False
