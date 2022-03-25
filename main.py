# from pickle import TRUE
from turtle import Screen, onkey
import time
from gamer import Gracz
from obstacles import Obstacles

gramy = True

ekran = Screen()
ekran.setup(600, 600)
ekran.bgcolor("black")
ekran.title("Crossy Road")
ekran.tracer(0)
t = Gracz()
x = -285
y = 0

o1 = Obstacles(x, -100)
o2 = Obstacles(x, 100)
oTab = [o1, o2]
# t.obstacles = [onkey]
while True:
    ekran.update()
    time.sleep(0.05)

    while -285 <= oTab.o.position()[0] < 290:
        ekran.update()
        oTab.o.forward(25)
        time.sleep(0.1)
        if oTab.o.distance(t.gm.position()) < 20:
            print("PRZEGRANA")
            time.sleep(1)
            ekran.bye()
            break
    while oTab.o.position()[0] >= 290 or oTab.o.position()[0] > -280:
        ekran.update()
        oTab.o.forward(-25)
        time.sleep(0.1)

    if oTab.o.distance(t.gm.position()) < 20:
        print("PRZEGRANA")
        time.sleep(1)
        ekran.bye()
        break




    ekran.listen()
    ekran.onkeypress(t.gora, "Up")
    ekran.onkeypress(t.dol, "Down")
    ekran.onkeypress(t.lewa, "Left")
    ekran.onkeypress(t.prawa, "Right")

ekran.exitonclick()



