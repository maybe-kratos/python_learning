from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour :")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
yy = int(-70)
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=yy)
    yy += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won, the {} is the winner".format(winning_color))
            else:
                print("You have lost, the {} is the winner".format(winning_color))

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)



screen.exitonclick()
