import random
from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_random_car(self, min_y=-220, max_y=220, x=300):
        color = choice(COLORS)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.shape("square")
        turtle.color(color)
        turtle.turtlesize(
            stretch_wid=1,
            stretch_len=2
        )
        turtle.penup()
        turtle.goto(x=x, y=random.randint(min_y, max_y))
        turtle.showturtle()
        turtle.setheading(180)
        self.cars.append(turtle)

    def move_cars(self, level, max_x=-350):
        for car in self.cars:
            distance = ((level-1) * MOVE_INCREMENT) + STARTING_MOVE_DISTANCE
            car.forward(distance)
            if car.xcor() < max_x:
                car.clear()
                self.cars.remove(car)
