# 1. В первую очередь я бы проверил соединение с сервером. Потом просмотрел бы логи сервера (backend), какие ошибки он выдает.

# 2. Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код, с использованием типизации.

from typing import Generator

# вариант a: Передача аргумента по имени lambda step=step: callback(step)
def create_handlers(callback: callable) -> list:
    handlers: list = []
    for step in range(5):
        handlers.append(lambda step=step: callback(step))
    return handlers

def execute_handlers(handlers: list[callable]) -> None:
    for hendler in handlers:
        hendler()
    return

# вариант b: В функции create_handlers создаем генератор
def create_handlers(callback: callable) -> Generator:
    handlers: Generator = (
        lambda step=step: callback(step) for step in range(5)
    )
    return handlers

def execute_handlers(handlers: Generator) -> None:
    for hendler in handlers:
        hendler()
    return

# 3. Сколько HTML-тегов в коде на главной странице сайта greenatom.ru? Сколько из них содержит атрибуты?

from bs4 import BeautifulSoup
import requests

def tags(url: str) -> list:
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.content, features="html.parser")
        
    return soup.find_all(True)

all_tegs = tags('https://greenatom.ru/')
all_tegs_param = [i for i in all_tegs if len(i.attrs)]

# print(f'Количество тегов на сайте greenatom.ru: {len(all_tegs)}')
# print(f'Количество тегов с параметрами: {len(all_tegs_param)}')

# 4. Напиши функцию, которая возвращает текущий публичный IP-адрес компьютера.

def public_ip(url: str) -> str:
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text        

# print(public_ip('https://ifconfigt.me/'))

# 5. Напиши функцию, выполняющую сравнение версий.


def version_comparison(a: str, b: str ) -> int:
    if a == b:
        return 0
    else:
        if a < b:
            return -1
        else:
            return 1

# print(version_comparison('1.10.11', '1.10.1'))