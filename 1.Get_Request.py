
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(
    f'Status code: {response.status_code}'
)

print(
    f'First post: {response.json()[0]}'
)
print(
    f'Second post: {response.json()[1]}'
)

# Homework
# 📥 Часть 1: GET-запросы (чтение данных)

url = "https://jsonplaceholder.typicode.com"

# 🧠 GET-задания:
# 	1.	Получи список всех пользователей (/users) и выведи имена.
# 	2.	Выведи email всех пользователей.
# 	3.	Найди и выведи имя пользователя с id = 3.
# 	4.	Выведи названия всех задач (/todos) с userId = 1.
# 	5.	Подсчитай, сколько задач уже выполнено (completed = true).
# 	6.	Найди пост (/posts) с id = 5 и выведи его title и body.
# 	7.	Получи все комментарии к посту id = 10.
# 	8.	Выведи названия всех альбомов (/albums) пользователя с id = 2.
# 	9.	Найди пользователя по username = Bret и выведи его email.
# 	10.	Получи все фото (/photos) из альбома с id = 1 и выведи ссылки url.

# 	1.	Получи список всех пользователей (/users) и выведи имена.

import requests

respose_1 = requests.get('https://jsonplaceholder.typicode.com/users/')
for user in respose_1.json():
    print(user)

# 	2.	Выведи email всех пользователей.

for user in respose_1.json():
    print(f'{user["name"]}: {user["email"]}')


# 	3.	Найди и выведи имя пользователя с id = 3.

for user in respose_1.json():
    if user["id"] == 3:
        print(
            f'{user}'
        )

# 	4.	Выведи названия всех задач (/todos) с userId = 1.
respose_2 = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
for user in respose_2.json():
    print(user)
