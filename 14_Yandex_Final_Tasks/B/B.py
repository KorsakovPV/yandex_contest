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


class Solution:
    def bitwise_sorting(self, data):
        length = len(str(max(data)))
        rang = 10
        for i in range(length):
            sort_data = [[] for k in range(rang)]
            for item in data:
                figure = item // 10 ** i % 10
                sort_data[figure].append(item)
            data = []
            for index in range(rang):
                data = data + sort_data[index]
        return ' '.join(list(map(str, data)))


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = list(map(int, input_file[1].rstrip().split()))
    sol = Solution()
    return sol.bitwise_sorting(data)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '0 2 24 45 66 75 90 802', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '0 1 12 37 50', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '2 6 7 25 36', 'input3.txt error\n' + str(
        main(input_file))
