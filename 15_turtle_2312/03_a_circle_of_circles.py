from turtle import *


def draw_circle_of_circles(obj, num_circles, circle_rad):
    for i in range(num_circles):
        obj.circle(circle_rad)
        obj.up()
        obj.fd(circle_rad * 1.5)
        obj.down()
        obj.lt(360 / num_circles)

t = Turtle()
t.speed(0)

draw_circle_of_circles(t, 30, 30)

done()

