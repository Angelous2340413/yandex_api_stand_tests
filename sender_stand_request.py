# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
import requests
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)

# Вызов функции post_new_user для создания нового пользователя
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
print(response.status_code)

# Вывод ответа в формате JSON
print(response.json())

# Определение функции для отправки GET-запроса на получение данных из таблицы пользователей
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Вызов функции для получения данных из таблицы пользователей
response = get_users_table()

# Вывод HTTP-статус кода ответа
print(response.status_code)
