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

https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


def solution(n, k):
    if n == 1:
        return 0
    if k <= 2 ** (n - 1) / 2:
        return solution(n - 1, k)
    else:
        return 1 - solution(n - 1, k - 2 ** (n - 1) / 2)


    return str(solution(n, k))


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    n = int(input_file[0])
    k = int(input_file[1])
    return str(solution(n, k))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt))

    assert main(
        'input1.txt') == '0', 'input1.txt error\n' + str(main(
        'input1.txt'))
    assert main('input2.txt') == '1', 'input2.txt error\n' + str(main(
        'input2.txt'))
