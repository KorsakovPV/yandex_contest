"""
G. Периметр треугольника

Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел, в
котором каждый элемент обозначает длину стороны треугольника. Нужно определить
максимально возможный периметр треугольника, составленного из сторон с длинами
из заданного массива. Помогите Рите скорее закончить игру и пойти спать.

Формат ввода
В первой строке записано n - целое число, не превосходящее 10000 Во второй
строке записаны n неотрицательных целых чисел, каждое из которых не превосходит
10000.

Формат вывода
Нужно вывести наибольший периметр треугольника, который возможно составить из
сторон с заданными длинами.
"""


def solution(list_triangle):
    list_triangle.sort(reverse=True)
    index = 0
    while len(list_triangle) - 3 >= index:
        amount = list_triangle[index] + list_triangle[index + 1] + \
                 list_triangle[index + 2]
        if amount - list_triangle[index] > list_triangle[index]:
            return amount
        index += 1


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    list_triangle = list(map(int, input_file[1].rstrip().split()))
    sol = solution(list_triangle)
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
        input_file) == '8', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '20', 'input2.txt error\n' + str(
        main(input_file))

    # with open('input3.txt') as f:
    #     input_file = f.read()
    # assert main(input_file) == '2 6', 'input3.txt error\n' + str(
    #     main(input_file))
