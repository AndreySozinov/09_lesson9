# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.
from typing import Callable
import json


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        parameters = []

        json_dict = {'args': args, **kwargs, 'result': result}
        parameters.append(json_dict)

        with open(f'{func.__name__}.json', 'a+', encoding='utf-8') as f:
            json.dump(parameters, f, ensure_ascii=False, indent=2)
        return result
    return wrapper


@deco
def my_func(*args, **kwargs) -> str:
    return f'Функция отработала.'


if __name__ == '__main__':
    my_func(52, 2, 11, 6, tora=5, bible=14)
