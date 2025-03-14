from api import ApiGoogleMap

class TestGoogleMapApi:
    def test_api(self):
        start_api = ApiGoogleMap()
        place_id_list = []
        place_id_file_updated = []

        # Считали 5 place_id в список
        try:
            with open('file_id.txt', 'r') as file:
                place_id_file = file.read().split()
                print('Список считали из файла')
        except FileNotFoundError:
            print('Файл не найден')
        except PermissionError:
            print('Нет прав доступа к файлу')
        except IOError:
            print('Ошибка чтения из файла')

        # Удалили 2-ю и 4-ю локацию
        response_delete_1 = start_api.delete_location(place_id_file[1])
        assert response_delete_1.status_code == 200, 'Ошибка! Статус код DELETE некорректен!'
        print('Статус код DELETE корректен')
        response_delete_2 = start_api.delete_location(place_id_file[3])
        assert response_delete_2.status_code == 200, 'Ошибка! Статус код DELETE некорректен!'
        print('Статус код DELETE корректен')

        # Проверили 5 place_id и сохраняем существующие в список
        for one_place_id in place_id_file:
            response_get = start_api.check_location(one_place_id)
            if response_get.status_code == 200:
                print(f'Локация {one_place_id} существует!')
                place_id_file_updated.append(one_place_id)
            elif response_get.status_code == 404:
                print(f'Локации {one_place_id}, не существует!')

        # Запись существующих локаций в новый файл
        print(f'Существующие локации {place_id_file_updated}')
        try:
            with open('place_id_updated.txt', 'w') as file:
                file.writelines(f'{one_place_id} ' for one_place_id in place_id_file_updated)
                print('Список отправлен в файл!')
        except PermissionError:
            print('Нет прав доступа к файлу')
        except IOError:
            print('Ошибка записи в файл!')


test = TestGoogleMapApi()
test.test_api()