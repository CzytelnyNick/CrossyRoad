from turtle import Turtle
import time


class Finish:
    line = Turtle("square")
    line.color("white")
    line.shapesize(0.2, 25)
    line.penup()
    line.goto(0, 250)


class Text:
    txt = Turtle()
    txt.color('white')
    txt.penup()
    txt.hideturtle()


class W:
    w = Turtle()
    w.color('white')
    w.penup()
    w.hideturtle()
    w.goto(-80, 0)


class Wi:
    wi = Turtle()
    wi.color('white')
    wi.penup()
    wi.hideturtle()
    wi.goto(0, 0)


class Win:
    win = Turtle()
    win.color('white')
    win.penup()
    win.hideturtle()
    win.goto(30, 0)


class Lose:
    ls = Turtle()
    ls.color('white')
    ls.penup()
    ls.hideturtle()
    ls.goto(100, 100)
