from turtle import *


def spider(obj, x, y, length, quan):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(quan):
        obj.fd(length)
        for i in range(3):
            obj.fd(length * 0.3)
            obj.left(120)
        obj.bk(length)
        obj.lt(360 / quan)


def spiral(obj, x, y, lines, angle):
    obj.up()
    obj.goto(x, y)
    obj.down()
    length = 3
    for i in range(lines):
        obj.fd(length)
        obj.rt(angle)
        length += 3


t = Turtle()
t.speed(0)

spiral(t, 0, 0, 100, 95)


done()