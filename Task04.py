# Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.
from typing import Callable
from random import randint as r
__all__ = ['guessing']


def count(param):
    def func_closure(func: Callable) -> Callable[[], None]:
        min_number = 1
        max_number = 100
        min_tries = 1
        max_tries = 10

        def wrapper(number, tries, *args, **kwargs):
            for _ in range(param):
                if number < min_number or number > max_number:
                    number = r(1, 100)
                if tries < min_tries or tries > max_tries:
                    tries = r(1, 10)
                func(number, tries, *args, **kwargs)
        return wrapper
    return func_closure


@count(3)
def guessing(number: int, tries: int) -> None:
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
