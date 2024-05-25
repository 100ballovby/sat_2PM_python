# определим кортеж для распаковки
numbers = tuple(range(8))
print(numbers)

first_number = numbers[0]
middle_numbers = numbers[1:-1]
last_number = numbers[-1]

print(first_number, middle_numbers, last_number)

# Python-way
first_number0, *middle_numbers0, last_number0 = numbers
print(first_number == first_number0)
print(middle_numbers == middle_numbers0)
print(last_number == last_number0)  # False - потому что звездочка превращает распакованные элементы в список
print(first_number0, middle_numbers0, last_number0)