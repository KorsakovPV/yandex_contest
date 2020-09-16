"""
E. Бессовестные тараканы

На этот раз нужно определить стартовые номера тараканов с учетом того, в
скольких именно забегах первой и второй категории одновременно они участвовали.
То есть, если таракан со стартовым номером 1 участвовал в двух забегах первой
категории, и в трех забегах второй категории, то номер 1 в ответе должен
встречаться два раза.

Формат ввода
В первой строке записано число n - длина первого списка. Во второй строке -
число m - длина второго списка. Оба числа не превосходят 10000 В следующих двух
строках через пробел записаны два списка соответствующей длины, состоящие из
чисел, не превосходящих 10000.

Формат вывода
Нужно в строку вывести стартовые номера тараканов с учетом того, как они
записаны в первом списке.
"""
from collections import Counter


def solution(list_cockroach1, list_cockroach2):
    hash_list_cockroach2 = Counter(list_cockroach2)
    answer = []
    for i in list_cockroach1:
        if hash_list_cockroach2[i] > 0:
            answer.append(i)
            hash_list_cockroach2[i] -= 1
    return answer


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])  # длинна первого списка
    m = int(input_file[1])  # длинна второго списка
    if n > 0:
        list_cockroach1 = list(map(int, input_file[2].rstrip().split()))
    else:
        return ''
        list_cockroach1 = []
    if m > 0:
        list_cockroach2 = list(map(int, input_file[3].rstrip().split()))
    else:
        list_cockroach2 = []
    sol = solution(list_cockroach1, list_cockroach2)
    return ' '.join(map(str, sol))


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '4 9 2 2', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '2 6', 'input3.txt error\n' + str(
        main(input_file))
