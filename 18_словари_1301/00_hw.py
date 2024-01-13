from datetime import datetime


birthday = datetime(2002, 11, 5)
today = datetime.today()
delta = today - birthday

print(delta.days)
print(delta.days * 24)

birthday_weekday = birthday.weekday()
print(birthday_weekday)
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

print(weekdays[birthday_weekday])

match birthday_weekday:
    case 0:
        print('Понедельник')
    case 1:
        print('Вторник')
    # ...

