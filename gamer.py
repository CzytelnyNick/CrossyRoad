from turtle import Turtle, Screen

Sqr = "square"
Col = "white"
pkt = 0

class Gracz():
    def __init__(self):

        self.gm = Turtle(Sqr)
        self.gm.color(Col)
        self.gm.penup()
        self.gm.goto(0, -200)

    def gora(self):
        if self.gm.heading() == 90:
            self.gm.forward(15)
        if self.gm.heading() != 90:
            self.gm.setheading(90)

    def dol(self):
        if self.gm.heading() == 270:
            self.gm.forward(15)
        if self.gm.heading() != 270:
            self.gm.setheading(270)
        # self.calculate_distance()

    def lewa(self):
        if self.gm.heading() == 180:
            self.gm.forward(15)
        if self.gm.heading() != 180:
            self.gm.setheading(180)
        # self.calculate_distance()

    def prawa(self):
        if self.gm.heading() == 0:
            self.gm.forward(15)
        if self.gm.heading() != 0:
            self.gm.setheading(0)
        # self.calculate_distance()
    # def g(self):
