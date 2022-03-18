# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 08:13:14 2022

@author: Unnique
"""

from turtle import Turtle, Screen

tim = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
