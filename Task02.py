# Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
from typing import Callable
from random import randint as r
__all__ = ['guessing']


def func_closure(func: Callable) -> Callable[[], None]:
    min_number = 1
    max_number = 100
    min_tries = 1
    max_tries = 10

    def wrapper(number, tries):
        if number < min_number or number > max_number:
            number = r(1, 100)
        if tries < min_tries or tries > max_tries:
            tries = r(1, 10)
        func(number, tries)
    return wrapper


@func_closure
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
