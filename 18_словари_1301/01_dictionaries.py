person = {
    'name': 'John',
    'surname': 'Doe',
    'age': 20,
    'city': 'Minsk',
}

# обращение к значению словаря
print(person['name'])

# заменить значение ключа
person['city'] = 'Belgrade'
print(person)

# удалить пару ключ-значение
del person['city']  # удаление ключа (с технической точки зрения)
print(person)

# добавление в словарь новой пары
person['budget'] = 2000
print(person)


# print(person['city']) <- так как ключ city удален, обращение к нему приведет к ошибке

