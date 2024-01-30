from turtle import Turtle, Screen
from time import sleep
from player import Player

screen = Screen()
player = Player()
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

screen.exitonclick()
