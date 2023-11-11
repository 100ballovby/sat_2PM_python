# кортеж - неизменяемая коллекция данных, защищенная от любого вмешательства

abilities = (100, 1, 200)
print(type(abilities))
print(abilities)
print(abilities[0])

# abilities[1] = 6 <- замена элементов невозиожна
# abilities.append(13)  <- добавить элемент нельзя
# удалить элемент нельзя
tmp = list(abilities)
tmp[1] = 200
abilities = tuple(tmp)
print(abilities)



