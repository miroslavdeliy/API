# Импортирование библиотеки
import requests

#Создание общего класса
class TestCreateJoke:
    url = "https://official-joke-api.appspot.com"

    #Метод для теста
    def test_create_random_joke(self):
        type_category = 'general'
        path_random_joke_general = f'/jokes/{type_category}/random'
        url_random_joke_general = self.url + path_random_joke_general
        print(url_random_joke_general)

        # Отправка запроса по категории general
        result = requests.get(url_random_joke_general)
        print(result.json())

        # Проверка корректности статус кода
        print(f'Статус-код: {result.status_code}')
        assert result.status_code == 200, 'Ошибка! Статус код некорректен!'
        print('Статус-код корректен')

        # Получение типа шутки
        check_joke = result.json()
        joke_type = check_joke[0].get('type')
        print(joke_type)

        # Проверка корректности типа шутки
        assert joke_type == type_category, 'Ошибка категории не совпали!'
        print('Категории совпали')

        print('Тест прошел успешно')


# Основное тело программы
start = TestCreateJoke()
start.test_create_random_joke()