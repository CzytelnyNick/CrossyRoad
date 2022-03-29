# from pickle import TRUE
import os
from turtle import Screen, Turtle
import time
from gamer import Gracz
from obstacles import Obstacles
import random
from finish import Finish, Text, W, Wi, Win, Lose

gramy = True

ekran = Screen()
ekran.setup(600, 600)
ekran.bgcolor("black")
ekran.title("Crossy Road")
ekran.tracer(0)
t = Gracz()
x = -285
y = 0
pkt = 0
i = 0
game = True
o1 = Obstacles(x, -100)
o2 = Obstacles(x, 100)
oTab = [o1, o2]
fnsh = Finish()
text = Text()
w = W()
wi = Wi()
win = Win()
lose = Lose()
wygrana = 1

text.txt.goto(-250, 200)
text.txt.write(f"WITAM, ABY WYGRAĆ PRZEJDŹ TOR 5 RAZY", font=("Arial", 17, "bold"))

time.sleep(5)
text.txt.clear()
while game:
    ekran.update()
    speed = random.randrange(25, 50)
    place = random.randrange(-90, 200)
    if i == 0:
        text.txt.write(f"RUNDA {pkt}", font=("Arial", 14, "bold"))
        time.sleep(0.1)
        text.txt.clear()

    ekran.listen()
    ekran.onkeypress(t.gora, "Up")
    ekran.onkeypress(t.dol, "Down")
    ekran.onkeypress(t.lewa, "Left")
    ekran.onkeypress(t.prawa, "Right")

    if t.gm.position()[1] >= 250:
        i = i + 1
        t.gm.goto(0, -200)

    if i == 1:
        o3 = Obstacles(x, place)
        oTab.append(o3)
        i = 0
        pkt = pkt + 1

    if pkt == 5:

        t.gm.hideturtle()
        for obj in oTab:
            obj.o.hideturtle()
        fnsh.line.hideturtle()
        text.txt.clear()
        time.sleep(2)
        game = 0

    for obj in oTab:
        if obj.kierunek == 1:
            ekran.update()
            obj.o.forward(speed)
            time.sleep(0.1)

        if obj.kierunek == 2:
            ekran.update()
            obj.o.back(speed)
            time.sleep(0.1)

        if -270 >= obj.o.position()[0]:
            obj.kierunek = 1

        if obj.o.position()[0] >= 270:
            obj.kierunek = 2

        if obj.o.distance(t.gm.position()) < 15:
            print("PRZEGRANA")
            time.sleep(1)
            ekran.bye()
            break
if wygrana == 1:
    while True:
        w.w.write("W", font=("Arial", 60, "bold"))

        time.sleep(1)

        wi.wi.write("I", font=("Arial", 60, "bold"))
        time.sleep(1)

        win.win.write("N", font=("Arial", 60, "bold"))
        time.sleep(1)

        ekran.exitonclick()
else:
    lose.ls.write("LOSE", font=("Arial", 60, "bold"))
    ekran.exitonclick()