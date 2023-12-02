from turtle import *
from tools import square   # импортировать из файла tools.py функцию square()


t = Turtle()
t.speed(0)
t.shape("turtle")

square(t, 50, 50, "#f1a3b2", 100, 100)
square(t, 200, 150, "#00D5DA", -250, 100)
square(t, 100, 50, "#00FF13", 170, -200)


done()
