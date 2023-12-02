def square(obj, width, height, color, x, y):
    obj.up()  # не рисовать
    obj.goto(x, y)  # перейти в координаты из параметров функции
    obj.down()  # рисовать
    obj.color(color)  # задать цвет
    for i in range(2):  # повторить 2 раза
        obj.fd(width)  # вперед
        obj.lt(90)  # влево
        obj.fd(height)
        obj.lt(90)

"""Старайтесь делать так, чтобы в функции не было 
ни одного фактического значения (числа, строки и прочее)"""
