"""
B. Фибоначчи с памятью

Функция из прошлого задания работала слишком долго. Нужно модифицировать ее
таким образом, чтобы одни и те же значения повторно не вычислялись.

Формат ввода
На вход подается число n.

Формат вывода
Напечатайте n-ное число Фибоначчи.

Примечания
Функция должна быть реализована рекурсивно.
"""


def fibonacci_numbers(n):
    assert n >= 0
    if n not in cache:
        cache[n] = 1 if n <= 1 else fibonacci_numbers(
            n - 1) + fibonacci_numbers(n - 2)
    return cache[n]

def main(input_file):
    with open(input_file) as f:
        input_file = int(f.read().rstrip().split()[0])

    return str(fibonacci_numbers(input_file))


if __name__ == '__main__':
    cache = {}
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == '3', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1', 'input2.txt error\n' + main(
        'input2.txt')
