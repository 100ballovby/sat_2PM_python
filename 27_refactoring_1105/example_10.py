from math import pi


def calculate_perimetr(length, width):
	"""
	Рассчитывает периметр прямоугольника
	:param length: длина прямоугольника
	:param width: ширина прямоугольника
	:return: периметр прямоугольника
	"""
	return 2 * (length + width)


def calculate_area_rectangle(length, width):
	"""
	Рассчитывает площадь прямоугольника
	:param length: длина прямоугольника
	:param width: ширина прямоугольника
	:return: площадь прямоугольника
	"""
	area = length * width
	perimetr = calculate_perimetr(length, width)
	return area, perimetr


def calculate_circle_area(radius):
	"""
	Рассчитывает площадь круга
	:param raidus: радиус круга
	:return: плошадь круга
	"""
	area = pi * radius ** 2
	perimetr = 2 * pi * radius
	return area, perimetr

