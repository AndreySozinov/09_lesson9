# Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.
from typing import Callable
from random import randint as r
import json
from functools import wraps
__all__ = ['guessing']


def count(param):
    def func_control(func: Callable) -> Callable[[], None]:
        min_number = 1
        max_number = 100
        min_tries = 1
        max_tries = 10

        @wraps(func)
        def wrapper(number, tries, *args, **kwargs):
            for _ in range(param):
                if number < min_number or number > max_number:
                    number = r(1, 100)
                if tries < min_tries or tries > max_tries:
                    tries = r(1, 10)
                func(number, tries, *args, **kwargs)
        return wrapper
    return func_control


def saving(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = []

        json_dict = {'args': args, **kwargs}
        parameters.append(json_dict)

        with open(f'{func.__name__}.json', 'a+', encoding='utf-8') as f:
            json.dump(parameters, f, ensure_ascii=False, indent=2)
    return wrapper


@saving
@count(3)
def guessing(number: int, tries: int) -> None:
    """Game - Catch the number."""
    success = False
    for i in range(tries):
        one_try = int(input(f'Угадай число. Осталось попыток: {tries - i}\n'))
        if one_try < number:
            print('Слишком мало.')
        elif one_try > number:
            print('Слишком много.')
        else:
            print(f'Угадал за {i + 1} попыток!')
            success = True
            break
    if not success:
        print(f'Сожалею, попытки закончились. Загаданное число: {number}')


if __name__ == '__main__':
    guessing(120, 0)
