from turtle import *
import random as r

colormode(255)
t = Turtle()
t.speed(0)

dist = 5
col = [r.randint(200, 255), r.randint(200, 255), r.randint(200, 255)]
print(col)
while col[0] > 0 and col[1] > 0 and col[2] > 0:
    t.color(*col)
    col[0] -= 1
    col[1] -= 2
    col[2] -= 5
    t.fd(dist)
    t.lt(90)
    dist += 5

done()
