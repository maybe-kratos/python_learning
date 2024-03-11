from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.CAR_SPEED = MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=330, y=random_y)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.fd(STARTING_MOVE_DISTANCE)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.fd(self.CAR_SPEED)

    def level_up(self):
        self.CAR_SPEED += 5
