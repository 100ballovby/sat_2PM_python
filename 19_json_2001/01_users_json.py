import requests as req


url = 'https://jsonplaceholder.typicode.com/users'
response = req.get(url)
r_json = response.json()  # позволяет обрабатывать ответ от сервера в виде коллекции

todo_url = 'https://jsonplaceholder.typicode.com/todos'
todo_response = req.get(todo_url)
todo_json = todo_response.json()



for user in r_json:
    print(user)
    text = f'''\t\t\tEmployee Card
    id: {user['id']}
    Name: {user['name']}
    Email: {user['email']}
    Phone: {user['phone']}
    Works: {user['company']['name']}
    '''
    with open(f'users/user_{user["username"]}.txt', 'w') as outfile:
        outfile.write(text)


for user in r_json:  # перебираю словари с информацией о пользователях
    user_id = user['id']  # фиксирую уникальный идентификатор пользователя в переменной
    for todo in todo_json:  # перебираю словари с информацией о задачах
        if todo['userId'] == user_id:  # если задача в поле userId имеет число, совпадающее с идентификатором пользователя
            print(f'Task "{todo["title"]}" is for user {user["username"]}')  # пишу текст

