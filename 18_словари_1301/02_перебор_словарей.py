weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

weekdays_dict = dict(zip(range(7), weekdays))
with open('smth.py', 'w') as f:
    f.write(str(weekdays_dict))
