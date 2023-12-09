def draw_circle(obj, x, y, rad):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad)


def draw_circle_pro(obj, x, y, rad, ext=360):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad, ext)
