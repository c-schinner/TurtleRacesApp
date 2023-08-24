from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)


turtle_color = ["blue", "red", "black", "purple", "orange", "green"]
y_start = [-60, -30, 0, 30, 60, 90]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-225, y=y_start[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n Choose a Turtle: ")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} turtle was correct")
            else:
                print(f"You lose, The correct turtle was {winning_turtle}")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
