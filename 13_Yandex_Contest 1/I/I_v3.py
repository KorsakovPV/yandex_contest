"""
I. Одинаковые суммы

Гоше стало интересно, можно ли разбить все заработанные им во время игры в
Лампу очки на две части так, чтобы сумма в них была одинаковой.

Формат ввода
В первой строке записано число элементов массива n. Оно не превосходит 10000

Далее в строку записаны n целых неотрицательных чисел, каждое из которых не
превосходит 10000

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе — False
"""


# Жадное решение
def split(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    array = [int(x) for x in s[1].split()]
    array.sort()
    array_amount = sum(array) / 2
    index = 0
    amount_one = 0
    # amount_two = 0
    while amount_one < array_amount:
        amount_one += array[index]
        index += 1

    return str(amount_one == array_amount) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(split(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == 'True\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == 'False\n', 'input2.txt error\n' + main(
        'input2.txt')
