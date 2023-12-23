from turtle import *


def lines(obj, x, y, length, direction):
    for i in range(length // 10):
        obj.up()
        obj.goto(x, y)
        obj.down()
        obj.fd(length)
        length *= 0.9
        y -= direction


def pyramid(obj, x, y, length, direction):
    for i in range(10):
        obj.up()
        obj.goto(x, y)
        obj.down()
        obj.fd(length)
        length *= 0.9
        y += direction
        x += length * 0.05


t = Turtle()
t.speed(0)

x, y, = 0, 0
leng = 100
direct = 10
pyramid(t, 0, 0, 100, 10)

done()
