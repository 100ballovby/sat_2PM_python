import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()  # вызываем функцию запуска виртуального окружения

token = os.environ.get("TOKEN")
domain = os.environ.get("DOMAIN")
print(token, domain)

# Вариант работы как со словарем
config = dotenv_values()  # по умолчанию берем .env
print(config)
print(config["TOKEN"])
print(config["DOMAIN"])

print()
print(os.getcwd())

