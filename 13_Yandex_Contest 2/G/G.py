"""
G. Недоалфавит

Евлампия не смогла разобраться с рекурсией! Напишите реализацию алгоритма
определения факториала числа с использованием цикла.

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 22

Формат вывода
Нужно вывести число - факториал для n

"""
from string import ascii_lowercase


def alphabet(n):
    for i in ascii_lowercase:
        if i == n:
            print(i, end=' ')
            break
        else:
            print(i, end=' ')
    return None


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip()
    return str(alphabet(input_file))


if __name__ == '__main__':
    cache = {}
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    # assert main(
    #     'input1.txt') == 'a b c d e f g h i j k l m n o p q r s t u v w x y z', 'input1.txt error\n' + main(
    #     'input1.txt')
    # assert main('input2.txt') == 'a b c', 'input2.txt error\n' + main(
    #     'input2.txt')
