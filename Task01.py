# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from typing import Callable
from random import randint as r
__all__ = ['func_closure']


def func_closure(border: int = 100, tries: int = 10) -> Callable[[], None]:
    def guessing():
        success = False
        number = r(1, border)
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
    return guessing


if __name__ == '__main__':
    game1 = func_closure()
    game1()
