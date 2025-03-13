import requests

class TestNewLocation:
    # Конструктор
    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'
        self.post_resourse = '/maps/api/place/add/json'
        self.get_resourse = '/maps/api/place/get/json'
        self.put_resourse = '/maps/api/place/update/json'
        self.new_address = '50 Sovetskay street, RU'
        self.place_id = ''

    # Метод создания новой локации
    def test_create_new_location(self):
        post_url = self.base_url + self.post_resourse + self.key
        print(post_url)
        json_location = {
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

        # Запрос POST
        result_post = requests.post(post_url, json=json_location)
        print(result_post.json())
        print(f'Статус-код: {result_post.status_code}')

        # Проверка статус кода
        assert result_post.status_code == 200, 'Ошибка! Статус код POST некорректен'
        print('Статус-код POST корректен')

        # Проверка поля Status
        check_response_post = result_post.json()
        status = check_response_post.get('status')
        print(status)
        assert status == 'OK', 'Ошибка! Поле status некорретно'
        print('Поле Status корректно')

        # Сохрание place_id
        self.place_id = check_response_post.get('place_id')
        print(f'Поле place_id: {self.place_id}')

    # Метод проверки созданной локации
    def test_check_created_location(self):
        get_url = self.base_url + self.get_resourse + self.key + '&place_id=' + self.place_id
        print(get_url)

        # Запрос GET
        result_get = requests.get(get_url)
        print(result_get.json())
        print(f'Статус-код: {result_get.status_code}')

        # Проверяем статус код локации
        assert result_get.status_code == 200, 'Ошибка! Статус код GET некорректен!'
        print('Статус код GET корректен')

    # Метод обновления адреса локации
    def test_update_location(self):
        put_url = self.base_url + self.put_resourse + self.key
        print(put_url)
        json_put_location = {
            "place_id" : self.place_id,
            "address" : self.new_address,
            "key" : "qaclick123"
        }

        # Запрос PUT
        result_put = requests.put(put_url, json=json_put_location)
        print(result_put.json())
        print(f'Статус-код: {result_put.status_code}')

        # Проверка статус кода запроса
        assert result_put.status_code == 200, 'Ошибка! Статус код PUT некорректен'
        print('Статус-код PUT корректен')

        # Проверка поле "msg" в ответе
        check_response_put = result_put.json()
        msg = check_response_put.get('msg')
        print(msg)
        assert msg == 'Address successfully updated', 'Ошибка! Поле MSG некорректно'
        print('Поле MSG корректно')

    # Метод проверки обновленной локации
    def test_check_updated_location(self):
        get_url = self.base_url + self.get_resourse + self.key + '&place_id=' + self.place_id
        result_get = requests.get(get_url)
        print(result_get.json())

        # Запрос GET
        check_response_get = result_get.json()
        print(f'Статус-код: {result_get.status_code}')

        # Проверка статус кода
        assert result_get.status_code == 200, 'Ошибка! Статус код GET некорректен'
        print('Статус код GET корректен')

        # Проверка нового адреса
        actual_address = check_response_get.get('address')
        print(actual_address)
        assert actual_address == self.new_address, 'Ошибка! Адрес в базе данных не изменился'
        print('Адрес изменился')