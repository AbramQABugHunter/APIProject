import json

from requests import Response

"""Методы для проверки ответов наших запросов"""


class Checking:
    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провалено!!! Cтатус код = {response.status_code}"
        print("Успешно!!! Cтатус код = " + str(response.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Успешно!!! Все поля присутствуют")

    """Метод для проверки содержимого обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!!!")

    """Метод для проверки заданого слова в содержимом обязательных полей ответа запроса"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"{search_word} присутствует!!!")
        else:
            print(f"{search_word} отсутствует!!!")