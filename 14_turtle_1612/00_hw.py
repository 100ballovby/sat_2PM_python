from turtle import *
from hw_staff import draw_cricle


t = Turtle()
t.speed(0)


x, y = -100, 10
rad = 100
t.pensize(rad * 0.15)
for i in range(4):
    draw_cricle(t, x, y, rad)
    x += rad * 1.3

done()
