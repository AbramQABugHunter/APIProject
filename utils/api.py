from utils.http_methods import HttpMethods

"""методы для тестирования GoogleMapsAPI"""

BASE_URL = "https://rahulshettyacademy.com"  # Базовая URL
KEY = "?key=qaclick123"  # Параметр для всех запросов


class GoogleMapsAPI:
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"  # Ресурс метода POST
        post_url = BASE_URL + post_resource + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # Ресурс метода GET
        get_url = BASE_URL + get_resource + KEY + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place(place_id):
        json_for_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_resource = "/maps/api/place/update/json"  #Ресурс метода PUT
        put_url = BASE_URL + put_resource + KEY
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put


    """Метод для удаления новой локации"""
    @staticmethod
    def delete_new_place(place_id):
        json_for_delete_new_place = {
            "place_id": place_id
        }
        delete_resource = "/maps/api/place/delete/json"     #Ресурс метода DELETE
        delete_url = BASE_URL + delete_resource + KEY
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_place)
        print(result_delete.text)
        return result_delete


