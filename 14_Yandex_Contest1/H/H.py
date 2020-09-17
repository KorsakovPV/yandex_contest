"""
H. Клумбы

Евлампия захотела, чтобы у нее под окном были клумбы с одуванчиками. Для работ
по подготовке земельного участка под клумбы было нанято n садовников.
Каждый из садовников обрабатывал какой-то участок земли. Процесс был
организован не очень хорошо, иногда один и тот же участок, или часть участка
мог быть обработан сразу несколькими садовниками. Обработанный участок любого
размера становился клумбой. В клумбе не могло быть необработанных промежутков.
Нужно определить границы получившихся клумб.

Формат ввода
В первой строке задано количество садовников - n. Число садовников не
превосходит 1000 В следующих n строках через пробел записаны координаты
участков в формате:
start end Оба числа целые, неотрицательные, и не превосходят 1000. start не
может быть больше, чем end

Формат вывода
Нужно вывести в отдельной строке координаты каждой из получившихся клумб.
Данные должны выводится в отсортированном порядке.
"""


def solution(list_flowerbed):
    list_flowerbed.sort(reverse=True)
    answer = list()
    answer.append(list_flowerbed.pop())
    while len(list_flowerbed) > 0:
        flowerbed = list_flowerbed.pop()
        if answer[-1][1] < flowerbed[0]:
            answer.append(flowerbed)
        else:
            if answer[-1][0] > flowerbed[0]:
                answer[-1][0] = flowerbed[0]
            if answer[-1][1] < flowerbed[1]:
                answer[-1][1] = flowerbed[1]
    answer_str = ''
    for i in answer:
        answer_str += '{0} {1}\n'.format(i[0], i[1])

    return answer_str


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    list_flowerbed = list()
    for flowerbed in input_file[1:]:
        list_flowerbed.append(list(map(int, flowerbed.split())))
    sol = solution(list_flowerbed)
    return str(sol)


if __name__ == '__main__':
    with open('input2.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '2 3\n6 10\n', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '2 4\n5 5\n', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '0 0\n1 6\n', 'input3.txt error\n' + str(
        main(input_file))
