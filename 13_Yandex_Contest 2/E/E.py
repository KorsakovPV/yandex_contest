"""
E. Кондратиева система шифрования

Ещё один важный математический объект — факториал.
Факториал - это произведение чисел от 1 до n.
В Трешландии существует своя система кодирования - Кондратиева. Число в этой
системе кодируется через значение факториала. Дочь Кондратия, Евлампия,
использует эту систему для шифрования пароля от айфона. Помогите Евлампии
зашифровать пароль. Нужно написать рекурсивную реализацию функции, вычисляющей
факториал заданного числа.

Примечания
Решение должно быть реализовано с помощью рекурсивной функции.
"""


def factorial(n):
    assert n >= 0
    return 1 if n <=1 else factorial(n - 1) * n

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
