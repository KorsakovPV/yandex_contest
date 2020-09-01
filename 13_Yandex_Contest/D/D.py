"""
D. Ценный рюкзак

Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции.

Формат ввода
В первой строке записано целое число с в диапазоне от 0 до 1000 — вместимость
рюкзака.

Во второй — число n — количество предметов. Оно не больше 10000.

В следующих n строках записано по 2 числа, разделенные пробелом: стоимость
предмета и его вес. Оба числа не превосходят 1000

Формат вывода
Нужно в строке вывести в отсортированном порядке номера предметов, которые
будут выбраны. Номер предмета - это порядковый номер его появления во входных
данных. (Индексация начинается с нуля)

Примечания
Если стоимость предметов одинаковая, то выбираем предмет с меньшим весом. Если
при этом и вес одинаковый, выбираем тот, который пришел на вход первым.
"""


def valuable_backpack(input_file):
    s = input_file.strip().split('\n')
    weight_max, n = int(s[0]), int(s[1])
    data = s[2:]
    items = []
    weight_backpack = 0
    for i in range(len(data)):
        temp = data[i].split()
        items.append([i, int(temp[0]), int(temp[1])])

    backpack = []

    items.sort(key=lambda x: x[2], reverse=True)
    items.sort(key=lambda x: x[1])

    while items != []:
        temp = items.pop()
        if temp[2] <= weight_max - weight_backpack:
            weight_backpack += temp[2]
            backpack.append(temp)
        if weight_max - weight_backpack == 0:
            break

    output = ''

    backpack.sort(key=lambda x: x[0])
    for i in backpack:
        output += str(i[0]) + ' '

    return output.rstrip() + '\n'


def main(input_file):
    # f = open(input_file)
    with open(input_file) as f:
        input_file = f.read()
    # f.close()

    return str(valuable_backpack(input_file))


if __name__ == '__main__':
    input_txt = 'input2.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    f.close()

    # print(main(input_txt))

    assert main('input1.txt') == '3\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1 2 3\n', 'input2.txt error\n' + main(
        'input2.txt')
