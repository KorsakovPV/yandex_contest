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
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return ' '.join(map(str, data))


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = list(map(int, input_file[1].rstrip().split()))
    sol = solution(n, data)
    return str(sol)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '-30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '-19 -17 -16 -1 2 3 5 5 6 7 8 11 19 20 22', 'input2.txt error\n' + str(
        main(input_file))

    # with open('input3.txt') as f:
    #     input_file = f.read()
    # assert main(input_file) == '542210', 'input3.txt error\n' + str(
    #     main(input_file))
