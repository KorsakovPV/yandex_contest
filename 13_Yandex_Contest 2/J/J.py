"""
J. Кондратиева Грамматика

В Тупограде объявлено о проведении соревнования. Уехать навсегда из города
сможет тот, кто напишет самое эффективное решение задачи:
В первой строке записано число 0. Для того, чтобы понять, что записано в
следующей строке, нужно посмотреть на предыдущую, и изменить каждый 0 на 01, и
каждую 1 на 10.
Формат ввода
В первой строке записано n - число, не превосходящее 30. Во второй строке
записано k - число в диапазоне [1, 2^(N−1)].

Формат вывода
Нужно вывести k-ый символ в n-ой строке.

Примечания
Индексация начинается с 1 (для N и для K).
"""


def solution(n, k):
    in_str = list()
    in_str.append('0')
    out_str = list()
    for i in range(n):
        for j in in_str:
            if j == '0':
                out_str.append('0')
                out_str.append('1')
            elif j == '1':
                out_str.append('1')
                out_str.append('0')
        in_str = out_str
        out_str = list()

    return in_str[k - 1]


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    n = int(input_file[0])
    k = int(input_file[1])
    return solution(n, k)


if __name__ == '__main__':
    input_txt = 'input1.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt))

    assert main(
        'input1.txt') == '0', 'input1.txt error\n' + str(main(
        'input1.txt'))
    assert main('input2.txt') == '1', 'input2.txt error\n' + str(main(
        'input2.txt'))
