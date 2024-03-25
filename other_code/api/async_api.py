import asyncio

import aiohttp
import requests as requests

TOKEN_URL = 'https://jetlend.ru/wp-content/uploads/1c_token.txt'


def get_headers():
    response = requests.get(TOKEN_URL)
    token = response.text.strip()
    print("Полученный токен:", token)
    headers = {'Authorization': f'Token {token}'}
    return headers

async def fetch_json_chunk(url, session, headers):
    async with session.get(url, headers=headers) as response:
        # Проверяем успешность запроса
        if response.status != 200:
            raise Exception(f"Ошибка запроса: {response.status}")

        # Читаем JSON данные по частям
        async for chunk in response.content.iter_any():
            yield chunk


async def read_large_json(url, headers):
    with open("rezult.txt", "w") as rez:
        async with aiohttp.ClientSession() as session:
            async for chunk in fetch_json_chunk(url, session, headers):
                part = chunk.decode("utf-8")
                rez.write(part)



headers = get_headers()
# Запуск асинхронного чтения JSON данных
asyncio.run(read_large_json('https://jetlend.ru/lend/api/export/1c/payments', headers=headers))
# h1 = {'Authorization': 'Token 943297fcddf785fc56da07c131e20e9d1d449629'}
