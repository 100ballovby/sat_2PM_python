def draw_cricle(obj, x, y, rad):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad)