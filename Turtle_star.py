# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:17:52 2022

@author: Unnique
"""

# Turtle Star

from turtle import Turtle, Screen, begin_fill, end_fill, done, color, forward, left, pos

tim = Turtle()

tim = color('red', 'yellow')

tim = begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
screen = Screen()
screen.exitonclick()
