import sender_stand_request
import data

def get_kit_body(kit_name):
        current_body = data.kit_body.copy()
        current_body["name"] = kit_name
        return current_body
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

# Функция для позитивной проверки
def positive_assert(kit_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(kit_name)
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.json()["name"] == kit_name
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201

# Функция для негативной проверки
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.json()["name"] == kit_name
    assert kit_response.status_code == 400

# Функция для проверки без параметра
def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все параметры были переданы"

#1
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")
#2
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#3
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")
#4
def test_create_kit_512_letter_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
#5
def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")
#6
def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert("Мария")
#7
def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert('"№%@",')
#8
def test_create_kit_space_in_kit_name_get_success_response():
    positive_assert("Человек и КО ")
#9
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")
#10
def test_create_kit_without_kit_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

#11
def test_create_kit_wrong_type__kit_name_get_error_response():
    negative_assert_code_400(123)
