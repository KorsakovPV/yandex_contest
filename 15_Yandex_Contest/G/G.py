"""
G. Минимальные суммы

Даны 2 массива, отсортированные по неубыванию, а также число k. Нужно
определить пары, которые имеют наименьшую сумму. При этом пара должна состоять
из одного элемента первого массива, и одного элемента второго. Нужно найти k
таких пар с наименьшей суммой.

Формат ввода
В первой строке записано число n1 - длина первого массива.
Во второй строке через пробел записаны числа первого массива.
Далее записано число n2 - длина втрого массива.
В четвертой строке через пробел записаны числа второго массива.
В последней строке записано число k.
n1 и n2 не превосходят 1000, числа в массивах не превосходят 3000.
k не превосходит число возможных пар.

Формат вывода
Нужно вывести получившиеся пары в отсортированном порядке, каждую через пробел
в отдельной строке. Числа внутри пары также должны быть отсортированы. Общая
сортировка выполняется для уже отсортированных пар.
"""

import heapq


class Solution:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def min_amount(self, k):
        # answer_value = list()
        # item1 = heapq.heappop(self.data1)
        # item2 = heapq.heappop(self.data2)
        # answer_value.append(sorted([item1, item2]))
        # while len(answer_value) < k:
        #     if len(self.data1) <= 0:
        #         item2 = heapq.heappop(self.data2)#39
        #     elif len(self.data2) <= 0:
        #         item1 = heapq.heappop(self.data1)
        #     elif item1 + self.data2[0]<item2 + self.data1[0]:
        #         item2 = heapq.heappop(self.data2)#43
        #     else:
        #         item1 = heapq.heappop(self.data1)
        #
        #     answer_value.append(sorted([item1, item2]))

        # if index1 + 1 < len(self.data1) and index2 + 1 < len(self.data2):
        #     if self.data1[index1] + self.data2[index2 + 1] < self.data2[
        #         index2] + self.data1[index1 + 1]:
        #         index2 += 1
        #     else:
        #         index1 += 1
        #
        # elif index1 + 1 < len(self.data1) and index2 + 1 >= len(self.data2):
        #     index1 += 1
        #
        # elif index1 + 1 >= len(self.data1) and index2 + 1 < len(self.data2):
        #     index2 += 1


        answer_value = list()
        index1 = 0
        index2 = 0
        answer_value.append([self.data1[index1], self.data2[index2]])
        if index1+1 < len(self.data1):
            index1 += 1
        if index2+1 < len(self.data2):
            index2 += 1
        while len(answer_value) < k:
            if answer_value[-1][0]+self.data2[index2]<answer_value[-1][1]+self.data1[index1]:
                answer_value.append([answer_value[-1][0], self.data2[index2]])
                if index2+1 < len(self.data2):
                    index2 += 1
                else:
                    index1 += 1
            else:
                answer_value.append([self.data1[index1], answer_value[-1][1]])
                if index1+1 < len(self.data1):
                    index1 += 1
                else:
                    index2 += 1


        return answer_value


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n1 = int(input_file[0])
    if n1 == 0:
        return ''
    data1 = list(map(int, input_file[1].rstrip().split()))
    n2 = int(input_file[2])
    if n2 == 0:
        return ''
    data2 = list(map(int, input_file[3].rstrip().split()))
    k = int(input_file[4])
    heapq.heapify(data1)
    heapq.heapify(data2)
    sol = Solution(data1, data2)
    xx = sol.min_amount(k)
    aaa = ''
    for x in xx:
        aaa += str(x[0]) + ' ' + str(x[1]) + '\n'
    return aaa


if __name__ == '__main__':
    with open('input2.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(input_file) == '1 2\n1 4\n1 6\n', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(input_file) == '1 3\n2 3\n', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '1 1\n1 1\n', 'input3.txt error\n' + str(
        main(input_file))
