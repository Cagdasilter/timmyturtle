from turtle import Turtle, Screen
import random

screen = Screen()

is_game_on = False

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
all_turtles = []

screen.setup(width=500, height=400)
user_bet = screen.textinput("Turtle race!", "Choose your turtle: ")

y_position = -100

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-230, y_position)
    y_position += 30
    all_turtles.append(turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            if user_bet == turtle.pencolor():
                print(f"You win!, {turtle.pencolor()} turtle is the winner")
            else:
                print(f"You lose!, {turtle.pencolor()} turtle is the winner")
        turtle.forward(random.randint(1, 10))







screen.exitonclick()

