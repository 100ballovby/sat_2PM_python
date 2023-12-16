from turtle import *
from hw_staff import draw_cricle


t = Turtle()
t.speed(0)


x, y = -300, 0
rad = 30
t.pensize(rad * 0.15)
for i in range(10):
    draw_cricle(t, x, y, rad)
    x += rad * 2

t.up()
t.goto(-300, rad * 2)
t.down()
t.fd(rad * 18)

'''for i in range(10):
    t.circle(-100)
    t.fd(100)'''

done()
