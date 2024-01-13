import json


def json_to_collection(filename):
    with open(filename) as json_file:
        res = json.load(json_file)
    return res


def collection_to_json(obj, filename):
    """
    Функция превращает список или словарь Python в
    структуру формата JSON. Конкретно: трансформирует кавычки
    и расставляет отступы по объекту, чтобы его можно
    было сохранить в JSON-форме и передать для
    дальнейшей обработки
    :param obj: list/dict/tuple для трансформации
    :param filename: имя файла
    :return: None
    """
    json_str = json.dumps(obj, indent=4)  # превращает переданный объект в строку json
    with open(filename, 'w') as file:
        file.write(json_str)


file = json_to_collection('users.json')
print(type(file))
collection_to_json(file, 'new_users.json')
