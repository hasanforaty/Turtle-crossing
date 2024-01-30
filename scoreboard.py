from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def print_level(self):
        self.clear()
        self.goto(x=-200, y=250)

        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.print_level()

    def increase_level(self):
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
