# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
from typing import Callable
from random import randint as r
from functools import wraps


def solving_equation_from_csv(func) -> Callable[[], None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = []
        with (
            open('data.csv', 'r', newline='') as f_csv,
            open('results.json', 'w') as f_json
        ):
            csv_file = csv.reader(f_csv)
            for row in csv_file:
                a, b, c = row
                result = func(int(a), int(b), int(c), *args, **kwargs)
                json_dict = {'a': a, 'b': b, 'c': c, 'result': result}
                parameters.append(json_dict)
            json.dump(parameters, f_json, ensure_ascii=False, indent=2)
    return wrapper


@solving_equation_from_csv
def square_equation_solution(a: int, b: int, c: int) -> str:
    """Returns roots of the quadratic equation."""
    answer = ''
    d = b ** 2 - 4 * a * c
    if d < 0:
        answer = 'No roots.'
    elif d == 0:
        x = (-b) / (2 * a)
        answer = f'{x = }.'
    elif d > 0:
        x1 = ((-b) - d ** 0.5) / (2 * a)
        x2 = ((-b) + d ** 0.5) / (2 * a)
        answer = f'{x1 = } {x2 = }.'
    return answer


def numbers_gen_to_csv(amount: int = 100) -> None:
    """Write csv-file with data for square equation."""
    with open('data.csv', 'w', newline='') as f:
        for _ in range(amount):
            a = r(-100, 100)
            b = r(-100, 100)
            c = r(-100, 100)
            line = [a, b, c]
            csv_write = csv.writer(f)
            csv_write.writerow(line)


if __name__ == '__main__':
    numbers_gen_to_csv()
    square_equation_solution()
