import requests
from bs4 import BeautifulSoup


def start_count():

    # Ссылка на страницу
    url = "https://jetlend.ru/wp-content/uploads/jetlend.html"

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем HTML-код страницы
        html_content = response.text

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Находим все HTML-теги с атрибутами
        tags_with_attrs = soup.find_all(lambda tag: len(tag.attrs) > 0)

        # Выводим количество найденных тегов
        print("Количество HTML-тегов с атрибутами на странице:", len(tags_with_attrs))
    else:
        print("Не удалось получить доступ к странице.")


if __name__ == '__main__':
    start_count()
