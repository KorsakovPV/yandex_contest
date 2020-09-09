"""
F. Циклический факториал

Евлампия не смогла разобраться с рекурсией! Напишите реализацию алгоритма
определения факториала числа с использованием цикла.

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 22

Формат вывода
Нужно вывести число - факториал для n

"""


def factorial(n):
    assert n >= 0
    f = 1
    for i in range(n):
        f *= i + 1
    return f

def main(input_file):
    with open(input_file) as f:
        input_file = int(f.read().rstrip().split()[0])

    return str(factorial(input_file))


if __name__ == '__main__':
    cache = {}
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == '6', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1', 'input2.txt error\n' + main(
        'input2.txt')
