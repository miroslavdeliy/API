# Импортирование библиотеки
import requests

#Создание общего класса
class TestCreateJokeCategory:
    url = "https://api.chucknorris.io/jokes"

    #Метод для теста
    def test_create_random_joke(self, expected_status_code):
        # Запрос у пользователя категории
        category = input('Введите категорию, на которую хотите получить шутку: ')

        # Формирование url запроса на получение списка категорий
        path_list_categories = f"/categories"
        url_list_category = self.url + path_list_categories
        print(url_list_category)

        # Отправка запроса на получение списка категорий
        result_categories = requests.get(url_list_category)
        print(result_categories.json())

        # Проверка, что список категорий не пустой
        assert result_categories.json() != [], 'Ошибка! Список пустой!'
        print('Список не пустой')

        # Проверка статус код запроса
        assert result_categories.status_code == expected_status_code, 'Ошибка! Статус код некорректен!'
        print('Статус код корректен!\n')

        # Поиск введенной категории в списке категорий
        if category in result_categories.json():
            #Отправка запроса, если категория есть в списке
            url_random_joke_category = self.url + f"/random?category={category}"
            print(url_random_joke_category)
            result_random_joke_category = requests.get(url_random_joke_category)

            # Проверка статус кода запроса по категории
            print(f'Статус код по {category}: {result_categories.status_code}')
            assert result_random_joke_category.status_code == expected_status_code, f'Ошибка статус код запроса по {category} некорректен'
            print(f'Статус код по {category} корректен')

            # Проверка категории
            check_joke = result_random_joke_category.json()
            assert check_joke.get('categories')[0] == category, f'Ошибка! Категория {category} некорректна!'
            print(f'Категория {category} корректна!')

            # Вывод шутки
            print(f'Текст шутки: {check_joke.get('value')}\n')
        else:
            print('Ошибка! Данной категории нет в списке!')

        print('Тест завершен')


# Основное тело программы
start = TestCreateJokeCategory()
start.test_create_random_joke(200)