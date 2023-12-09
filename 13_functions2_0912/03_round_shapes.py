from turtle import *
from staff import draw_circle_pro


t = Turtle()
t.speed(0)
colormode(255)
ext = 60
rad = 20
r, g, b = 0, 10, 3
while r < 255 and g < 255 and b < 255:
    t.color(r, g, b)
    draw_circle_pro(t, 0, 0, rad, ext)
    ext += 2.5
    rad += 2.5
    t.rt(30)
    r += 5
    g += 5
    b += 15

done()
