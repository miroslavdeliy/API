from request_OOP import TestNewLocation

start = TestNewLocation()
# Создание новой локации
print('Тест начался!')
start.test_create_new_location()
# Проверка созданной локации
start.test_check_created_location()
# Обновление текущую локацию
start.test_update_location()
# Проверка обновленной локации
start.test_check_updated_location()
print('Тест прошел успешно')
