from turtle import *
from staff import draw_circle, draw_circle_pro
import random as r


t = Turtle()
t.speed(0)

x = 100
for i in range(4):
    draw_circle(t, x, 100, 50)
    x += 120

circles = r.randint(4, 80)
for i in range(circles):
    draw_circle(t, -100, -100, 50)
    t.rt(360 / circles)

t.lt(90)
x_coord = 200
for i in range(4):
    draw_circle_pro(t, x_coord, -200, 50, 180)
    t.rt(180)
    x_coord -= 100

done()
