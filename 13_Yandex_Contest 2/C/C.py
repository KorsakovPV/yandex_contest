"""
C. Эффективные числа Фибоначчи

У многих жителей Трешландии на компьютере осталось совсем мало свободного
места. Но они тоже хотят иметь возможность вычислять, сколько животных могут
завести. Нужно оптимизировать решение задачи про вычисление чисел Фибоначчи.
Объем дополнительной памяти должен быть O(1).

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 30.

Формат вывода
Решение должно работать за O(n) и использовать O(1) дополнительной памяти.s
"""


def fibonacci_numbers(n):
    assert n >= 0
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1

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
