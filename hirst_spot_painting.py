# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:42:48 2022

@author: Unnique
"""
# Program To generate colours list in the image.
# import colorgram

# rgb_colors = []

# colors = colorgram.extract('img.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# import turtle as turtl_module

# tim = turtle_module.Turtle()
import random
import turtle as turtle_module
import sys


turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed(0)
tim.penup()
tim.hideturtle()

color_list = [(211, 149, 97), (179, 67, 35), (14, 24, 42), (238, 209, 95), (235, 62, 35), (154, 26, 20), (72, 29, 33), (83, 93, 114), (67, 41, 35), (163, 141, 68), (125, 31, 37), (186, 82, 91), (135, 152, 163),
              (174, 57, 63), (49, 52, 126), (232, 171, 159), (162, 139, 148), (99, 114, 113), (17, 27, 27), (227, 169, 174), (160, 167, 165), (77, 70, 45), (188, 188, 202), (181, 198, 191), (122, 121, 144), (243, 200, 6)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

sys.exit()
