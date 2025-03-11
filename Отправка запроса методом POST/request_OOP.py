# Импорт необходимой библиотеки
import requests

# Создание общего класса
class test_new_location():
    # Метод для теста
    def test_create_new_location(self):
        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'
        place_id_list = []

        # Формирование запроса POST
        post_url = base_url + post_resourse + key
        print(post_url)
        # Body
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

        # Сохранение 5 place_id в список
        for _ in range(5):
            result_post = requests.post(post_url, json=json_location)
            assert result_post.status_code == 200, 'Ошибка! Статус код неверный!'
            print('Статус код POST корректный')
            check_response_post = result_post.json()
            print(check_response_post)
            place_id_list.append(check_response_post.get('place_id'))

        #Отправление списка в файл
        try:
            with open('place_id.txt', 'w') as file:
                file.writelines(f'{one_place_id} ' for one_place_id in place_id_list)
                print('Список отправлен в файл!')
        except PermissionError:
            print('Нет прав доступа к файлу')
        except IOError:
            print('Ошибка записи в файл!')

        #Чтение из файла и формирование списка
        try:
            with open ('place_id.txt', 'r') as file:
                place_id_file = file.read().split()
                print('Список считали из файла')
        except FileNotFoundError:
            print('Файл не найден')
        except PermissionError:
            print('Нет прав доступа к файлу')
        except IOError:
            print('Ошибка чтения из файла')

        # Отправка запроса GET по всем place_id из списка
        for one_place_id in place_id_file:
           get_url = base_url + get_resourse + key + '&place_id=' + one_place_id
           print(get_url)
           result_get = requests.get(get_url)
           print(result_get.json())
           print(f'Статус-код: {result_get.status_code}')
           assert result_get.status_code == 200, 'Ошибка Статус код GET некорректен!'
           print('Статус код GET корректен')


start = test_new_location()
start.test_create_new_location()
print('\nТест прошел успешно')