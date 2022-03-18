# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:39:16 2022

@author: Unnique
"""

from turtle import Turtle, Screen
import random
#import sys

is_race_on = False
#new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple", ]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    #new_turtle.goto(x=-230, y=-100)
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # print(turtle.color())
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost ! The {winning_color} turtle is the winner!")



        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
# sys.exit()
