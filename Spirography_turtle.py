# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:09:11 2022

@author: Unnique
"""

import turtle as turtle_module

import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# colours = ["sea green", "crimson", "magenta",
#            "orange red", "gold", "green", "navy"]


tim.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int((360/size_of_gap))):
        # tim.color(random.choice(colours))
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = turtle_module.Screen()
screen.exitonclick()
