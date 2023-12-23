from turtle import *


def cross(obj, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.fillcolor('red')
    obj.begin_fill()
    for i in range(4):
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)
        obj.fd(length)
        obj.rt(90)
    obj.end_fill()


def curve_cross(obj, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.fillcolor('red')
    obj.begin_fill()
    for i in range(3):
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)
        obj.fd(length)
        obj.rt(120)
    obj.end_fill()

t = Turtle()
t.speed(0)

curve_cross(t, 100, 100, 100)

done()
