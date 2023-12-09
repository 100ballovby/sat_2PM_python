from turtle import *


def x_angle(obj, angles, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    turn = 360 / angles
    for i in range(angles):
        obj.fd(length)
        obj.lt(turn)


t = Turtle()
t.speed(0)
t.shape("turtle")

x_angle(t, 4, 90, 90, 100)
x_angle(t, 3, -190, 90, 100)
x_angle(t, 5, 90, -190, 100)
x_angle(t, 9, 200, 190, 100)

done()
