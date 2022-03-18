# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:20:04 2022

@author: Unnique
"""

from turtle import Turtle
import random
tim = Turtle()

colours = ["sea green", "crimson", "magenta",
           "orange red", "gold", "green", "navy"]

#angle = [0, 90, 180, 270]

# num_sides = [3, 4, 5, 8]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        # tim.right(random.choice(angle))
        tim.right(angle)


for Shape_sides_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(Shape_sides_n)
