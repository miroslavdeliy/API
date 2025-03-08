# Импортирование библиотеки
import requests

# Печать url запроса
url = "https://official-joke-api.appspot.com/jokes/random"
print(url)

# Печать статус кода
result = requests.get(url)
print('Статус код: ' + str(result.status_code))

# Проверка корректности статус кода
assert 200 == result.status_code, 'Ошибка! Статус код не верен'
if result.status_code == 200:
    print('Успешно, статус код верен')
else:
    print('Провал, статус код не верен')

result.encoding = 'utf-8'
# Печать ответа на запрос в формате json
print(result.json())
