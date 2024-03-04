from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(5)


def move_backwards():
    tim.backward(5)


def rotate_clockwise():
    tim.right(10)


def rotate_anti_clockwise():
    tim.left(10)


def clear_screen():
    tim.home()
    tim.clear()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_anti_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
