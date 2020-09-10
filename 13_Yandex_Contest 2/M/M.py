"""
M. Земельный участок

Помогите Овощеславу определить максимально возможный размер квадратных
участков, на которые он может разделить свои владения.

Формат ввода
В первой стоке записана ширина участка, во второй - длина. Оба числа не
превосходят 10000.

Формат вывода
Нужно вывести максимально возможный размер квадратных участков, на который
можно разделить территорию.
"""


def solution(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    x = int(input_file[0])
    y = int(input_file[1])
    # coins = list(map(int, input_file[2].split()))
    return solution(x, y)


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))

    assert main('input1.txt') == 3, 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == 1, 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == 20, 'input3.txt error\n' + str(
        main('input3.txt'))
