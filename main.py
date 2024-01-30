from turtle import Turtle, Screen
from time import sleep
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
import random

screen = Screen()
player = Player()
car_manager = CarManager()
screen.setup(
    width=600,
    height=600,
)
screen.tracer(0)
screen.bgcolor("white")

screen.listen()
screen.onkeypress(
    player.move,
    'w'
)

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

    # create car
    cars_in_screen = len(car_manager.cars)
    create = random.randint(0, 3)
    if create == 0 and cars_in_screen < 40:
        car_manager.create_random_car()

    # move cars
    car_manager.move_cars(level=1)

    # check if player reached end point
    if player.ycor() > FINISH_LINE_Y:
        player.reset()
    # check for coalition with cars
    if car_manager.has_collided(player):
        game_is_on = False

screen.exitonclick()
