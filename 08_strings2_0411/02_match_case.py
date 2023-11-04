print('1 - наполнить\n2 - отсортировать\n3 - вывести\n4 - выйти')
choice = int(input('Сделайте свой выбор:'))

while choice > 0 and choice < 4:
    match choice:
        case 1:
            print('Наполнили')
        case 2:
            print('Отсортировали')
        case 3:
            print('Вывели')

    print('1 - наполнить\n2 - отсортировать\n3 - вывести\n4 - выйти')
    choice = int(input('Сделайте свой выбор:'))




