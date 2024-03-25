import requests

# Установка заголовка Authorization с токеном
headers = {
    'Authorization': 'Token 943297fcddf785fc56da07c131e20e9d1d449629'
}

# URL API, к которому вы обращаетесь
api_url = 'https://example.com/api/endpoint'

try:
    # Выполнение GET-запроса к API
    response = requests.get(api_url, headers=headers)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Данные успешно получены, можно работать с ответом
        data = response.json()
        print("Данные из API:", data)
    else:
        # Обработка ошибки запроса, если необходимо
        print("Ошибка при выполнении запроса:", response.status_code)

except requests.exceptions.RequestException as e:
    # Обработка ошибок, связанных с сетью или другими проблемами
    print("Ошибка сети:", e)

if __name__ == '__main__':
