import os


def find_and_read_file(top, filename):
    path = os.getcwd()  # получаем текущую директорию, в которой запускается файл
    for root, dirs, files in os.walk(top, topdown=False):  # просматриваем все составляющие файловой системы
        if filename in files:
            file_path = os.path.join(root, filename)  # складываем корневой путь и имя файла
            with open(file_path, 'r') as f:
                for line in f:
                    print(line)
            return  # если файл прочитается, то функция закончит работу здесь
    print('File not found!')


find_and_read_file('C:\\', 'cwdtext.txt')

