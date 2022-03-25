from turtle import Turtle

import time
import random

Sqr = "square"
Col = "white"

class Obstacles():
    def __init__(self, x, y):
        self.o = Turtle(Sqr)
        self.o.color(Col)
        self.o.penup()
        self.o.goto(x, y)
