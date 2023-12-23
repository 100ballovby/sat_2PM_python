from turtle import *


def draw_sierpinski_triangle(obj, order, size):
    for i in range(order):
        obj.fd(size)
        t.lt(120)


def draw_sierpinski(obj, iterations, initial_size):
    size = initial_size
    for i in range(iterations):
        draw_sierpinski_triangle(obj, 3, size)
        size /= 2
        obj.fd(size)
        t.lt(60)

t = Turtle()
draw_sierpinski(t, 4, 300)

done()
