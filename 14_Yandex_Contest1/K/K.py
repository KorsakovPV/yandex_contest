"""
K. Частичная сортировка

После того, как Гоша узнал про сортировку слиянием и быструю сортировку, он
решил придумать свой метод сортировки, который предполагал бы разделение данных
на части.
Назвал он свою сортировку Частичной.
Этим методом можно отсортировать n уникальных чисел, находящихся в диапазоне от
0 до n - 1.
В соответствии с методом нужно разбить данные на максимально возможное
количество частей таким образом, чтобы можно было отсортировать каждую из
частей отдельно, соединить, и при этом результат будет отсортирован.
После сортировки отдельных частей менять части местами нельзя.

Формат ввода
В первой строке задано n - количество чисел для сортировки.
В следующей строке записан числа от 0 до n - 1, которые нужно отсортировать
описанным методом.

Формат вывода
Выведите максимальное количество частей, на которое можно разбить данные при
использовании метода Частичной сортировки.
"""
from collections import Counter


def solution(list_input):
    print(1)



    return 0


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    list_input = list(map(int, input_file[1].split()))
    sol = solution(list_input)
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
        input_file) == '3', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '1', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '1', 'input3.txt error\n' + str(
        main(input_file))
