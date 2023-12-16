import random as r
from turtle import *
from staff import random_colors, spider


t = Turtle()
t.speed(0)

colors = random_colors(1000)

for i in range(500):
    x, y = r.randint(-500, 500), r.randint(-500, 500)
    d = r.randint(40, 100)
    t.up()
    t.goto(x, y)
    t.down()
    t.color(r.choice(colors))
    t.dot(d)

x, y = 0, 0
t.lt(90)
for i in range(3, 10):
    t.color(r.choice(colors))
    spider(t, x, y, 50, i)
    x = r.randint(-200, 200)
    y = r.randint(-200, 200)

done()
