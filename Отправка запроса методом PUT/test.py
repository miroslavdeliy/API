from api import ApiGoogleMap

class TestGoogleMapApi:

    # Метод проверки работы PUT
    def test_api(self):
        start_api = ApiGoogleMap()

        # Создание локации
        post_response = start_api.create_new_location()
        print(post_response.json())

        #Проверка статус кода POST
        print(f'Статус-код POST: {post_response.status_code}')
        assert post_response.status_code == 200, 'Ошибка! Статус код POST некорректен!'
        print('Статус код POST корректен!')

        check_response_post = post_response.json()

        # Проверка поля status в ответе
        status = check_response_post.get('status')
        print(status)
        assert status == 'OK', 'Ошибка запрос отработал неверно! Поле status некорректно!'
        print('Поле status корректно')

        place_id = check_response_post.get("place_id")
        print(f'Поле place_id {place_id}')

        # Проверка созданной локации
        get_response = start_api.check_location(place_id)
        print(get_response.json())

        # Проверка статус-кода запроса GET
        print(f'Статус-код GET: {get_response.status_code}')
        assert get_response.status_code == 200, 'Ошибка! Статус код запроса GET некорректен'
        print('Статус код GET корректен')

        actual_address = get_response.json().get('address')
        print(f'Актуальный адрес: {actual_address}')

        # Отправка запроса PUT
        put_response = start_api.update_location(place_id, '25 Lenina Street')
        print(put_response.json())

        # Проверка статус-кода
        print(f'Статус код PUT: {put_response.status_code}')
        assert put_response.status_code == 200, 'Ошибка! Статус код запроса PUT некорректен'
        print('Статус-код PUT корректен')

        check_response_put = put_response.json()

        # Проверка поле msg в ответе
        msg = check_response_put.get('msg')
        print(msg)
        assert msg == 'Address successfully updated'
        print('Поле MSG корректно')

        # Проверка изменений в базе данных
        get_response_result = start_api.check_location(place_id)
        print(get_response_result.json())
        check_response_get = get_response_result.json()

        # Проверка статус кода запроса GET
        print(f'Статус-код: {get_response_result.status_code}')
        assert get_response_result.status_code == 200, 'Ошибка! Статус-код GET некорректен'
        print('Статус-код GET корректен')

        new_address = check_response_get.get('address')
        print(new_address)
        assert new_address == '25 Lenina Street', 'Ошибка! Данные не сохранились в базе данных'
        print('Адрес изменился')

test = TestGoogleMapApi()
test.test_api()