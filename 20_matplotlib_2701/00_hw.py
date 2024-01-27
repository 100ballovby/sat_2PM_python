import requests as req


url = 'https://jsonplaceholder.typicode.com/users'
response = req.get(url)
r_json = response.json()  # позволяет обрабатывать ответ от сервера в виде коллекции

todo_url = 'https://jsonplaceholder.typicode.com/todos'
todo_response = req.get(todo_url)
todo_json = todo_response.json()


for user in r_json:  # перебираю словари с информацией о пользователях
    user_id = user['id']  # фиксирую уникальный идентификатор пользователя в переменной
    count_compl = 0
    count_incompl = 0
    for todo in todo_json:  # перебираю словари с информацией о задачах
        if todo['userId'] == user_id:  # если задача в поле userId имеет число, совпадающее с идентификатором пользователя
            if todo["completed"]:
                count_compl += 1
            else:
                count_incompl += 1
    kpi = count_compl / (count_compl + count_incompl) * 100
    print(f'User {user["username"]}. Completed {count_compl}, not completed {count_incompl}, kpi: {kpi}%')

