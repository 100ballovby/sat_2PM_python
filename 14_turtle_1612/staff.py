import random as r
import string


def random_colors(num):
    colors = []
    alph = string.digits + string.ascii_lowercase[:6]
    for i in range(num):
        color = '#'
        for j in range(6):
            color += r.choice(alph)
        colors.append(color)
    return colors


def spider(obj, x, y, length, quan):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(quan):
        obj.fd(length)
        obj.bk(length)
        obj.lt(360 / quan)


