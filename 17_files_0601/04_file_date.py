import os
import datetime as dt


def find_and_move_files(path):
    today = dt.date.today()  # фиксируем сегодняшнюю дату
    dir_name = f'{today}_dir'  # имя папки с сегодняшней датой

    if not os.path.exists(dir_name):  # если папка с таким именем не существует
        os.mkdir(dir_name)  # создаем папку с именем-сегодняшней датой

    for root, dirs, files in os.walk(path):  # перебираем ВСЁ в рабочей директории
        for file in files:  # перебираем файлы в файлах рабочей директории
            file_path = os.path.join(root, file)  # собираем путь к файлу из директории и названия файла
            file_date = os.path.getctime(file_path)  # возвращает время создания файла в формате timestamp
            file_date = dt.datetime.fromtimestamp(file_date)  # превращаем дату в нормальный формат
            if file_date.date() == today:  # если дата создания файла - сегодня
                new_path = os.path.join(dir_name, file)  # создаю новый путь из папки dir_name и названия файла
                os.replace(file_path, new_path)  # переместить файл в новый путь


find_and_move_files(os.getcwd())



