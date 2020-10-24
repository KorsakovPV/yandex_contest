"""
B. Radix Sort

Когда Кондратий узнал про алгоритм поразрядной сортировки, он объявил конкурс
на самую быструю реализацию алгоритма. Вы тоже принимаете участи в этом
конкурсе. Успехов!

Формат ввода
В первой строке задано n - длина массива неотрицательных целых чисел, каждое из
которых не превосходит 100000.
В следующей строке через пробел записаны n чисел.

Формат вывода
Выведите числа в отсортированном по неубыванию порядке.
"""


# 34647424
class Solution:
    def bitwise_sorting(self, data):
        length = len(str(max(data)))
        rang = 10
        for i in range(length):
            const = 10 ** i
            sort_data = [[] for _ in range(rang)]
            for item in data:
                figure = item // const % 10
                sort_data[figure].append(item)
            data = []
            for index in range(rang):
                data = data + sort_data[index]
        return data


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    data = list(map(int, input_file[1].rstrip().split()))
    sol = Solution()
    return ' '.join(list(map(str, sol.bitwise_sorting(data))))


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
