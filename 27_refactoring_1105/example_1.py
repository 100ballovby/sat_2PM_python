# создадим список чисел
numbers = list(range(8))
print(numbers)

# хочу сделать на основе списка чисел список квадратов чисел
squares = []
for number in numbers:
	if number % 2 == 0:
		squares.append(number * number)

print(squares)

# списковое включение
squares1 = [i * i for i in numbers if i % 2 == 0]
print(squares1)
