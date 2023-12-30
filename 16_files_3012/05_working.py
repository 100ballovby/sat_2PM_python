from file_func import read_file, write_file
import os

alice = read_file("alice.txt")
for line in alice:
    print(line)


directories = os.listdir()
new_path = os.path.dirname(os.path.realpath(__file__))
# ^ находит путь, по которому располагается файл (который запущен)
if 'System' in directories:
    write_file(new_path + "/System/virus.bat", 'Я вирус бубубубу!')

# На Windows пути к файлам пишутся так: C:\\Program Files\\...
# os.removedirs("System32") <- удалить папку
# os.remove('test.txt') <- удалить файл

