"""
A. Большое число

Вечером ребята решили поиграть в игру "Большое число".
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n - количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно из них составить.
"""


def solution(n, data):
    # for
    data.sort(reverse=True)
    return int(''.join(data))


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = input_file[1].rstrip().split()
    sol = solution(n, data)
    return str(sol)


def test():
    num = '998877665544332211'
    data = list()
    left = 1
    right = 0
    while left < len(num) // 2:
        data = list()
        data.append(num[0:left])
        data.append(num[left:-left - 1])
        data.append(num[-left: len(num)])
        print(data, solution(3, data))
        left += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    test()

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(input_file) == '56215', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(input_file) == '78321', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '542210', 'input3.txt error\n' + str(
        main(input_file))
