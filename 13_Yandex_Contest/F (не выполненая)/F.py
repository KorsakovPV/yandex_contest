"""
F. Отсортированные строки

После чая с печеньками ребята решили поиграть в игру. Дан набор строк
одинаковой длины, состоящих из маленьких латинских букв. Нужно определить,
какое минимальное число позиций в каждой из строк нужно удалить, чтобы буквы в
строках, соответствующие каждому индексу из оставшихся, были лексикографически
отсортированы по неубыванию.

Формат ввода
В первой строке записано число n - количество строк.

Во второй - m - длина каждой из строк.

Оба числа не превосходят 1000.

В каждой из следующих n строк записана строка, состоящая из m строчных букв
латинского алфавита.

Формат вывода
Нужно вывести одно число - минимальное количество индексов, которые нужно
удалить, чтобы выполнялось указанное требование.
"""


def сookies(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    m = int(s[1])
    strings = s[2:]
    n = s[0]
    answer = 0
    if m == 1:
        return str(0) + '\n'

    for string in strings:
        for s in range(m - 1):
            if ord(string[s]) <= ord(string[s + 1]):
                answer += 1
                s.pop()
                print(ord(string[s]))

    return str(0) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(сookies(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    f.close()

    assert main('input1.txt') == '1\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '0\n', 'input2.txt error\n' + main(
        'input2.txt')
