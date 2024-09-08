import configuration
import requests
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())
auth_token = response.json().get("authToken")

def post_new_client_kit (kit_body,auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=auth_headers)
response = post_new_client_kit(data.kit_body,auth_token)
print (response.status_code)
print(response.json())

