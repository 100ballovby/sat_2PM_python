import os


with os.scandir('2024-01-06_dir') as entries:  # .. <- на папку назад; . <- текущая директория
    for entry in entries:
        if entry.is_file():  # is_file() - определяет, является ли элемент файлом, is_dir() - папкой
            print(entry.name)




