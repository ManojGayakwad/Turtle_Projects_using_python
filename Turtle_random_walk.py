# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:04:16 2022

@author: Unnique
"""

# random Walk Using The turtle
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


directions = [0, 90, 180, 270]

#width = [1, 2, 3, 4, 5, 7, 8, 9, 10]

tim.pensize(8)
tim.speed(0)

for _ in range(400):
    tim.color(random_color())
    # tim.pensize(random.choice(width))
    # tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
