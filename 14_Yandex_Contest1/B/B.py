"""
B. Сортировка вставками

Теперь Гоша взялся за сортировку вставками.

Алгоритм следующий: На i-том шаге мы делаем так, чтобы первые i элементов
массива шли в возрастающем порядке.

1) На первом шаге ничего делать не нужно - один элемент и так "отсортирован".

2) На втором шаге нужно сделать так, чтобы два первых элемента были верно
отсортированы. То есть если второй элемент оказался меньше первого, их нужно
поменять местами.

3) На i - том шаге мы знаем, что первые i-1 элементов уже отсортированы. Ищем,
куда нужно вставить i-ый элемент.

Для этого, начиная с позиции j = i - 1, сравниваем текущий элемент с элементом
на позиции j. Пока j - й элемент больше i-ого и j > 0, меняем элементы местами,
и уменьшаем счетчик j на 1.

Помогите Гоше написать код.

Формат ввода
В первой строке на вход подается число n - длина массива. n не превосходит
1000. Во второй строке через пробел записаны n чисел. Каждое из чисел по модулю
не превосходит 1000.

Формат вывода
Нужно вывести через пробел числа в отсортированном по возрастанию порядке.
"""


def solution(n, data):
    for i in range(len(data)):
        revers = False
        min_index = i
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                revers = True
                min_index = j
        if revers:
            data[i], data[min_index] = data[min_index], data[i]

    return ' '.join(map(str, data))


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = list(map(int, input_file[1].rstrip().split()))
    sol = solution(n, data)
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
        input_file) == '-30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '-19 -17 -16 -1 2 3 5 5 6 7 8 11 19 20 22', 'input2.txt error\n' + str(
        main(input_file))

    # with open('input3.txt') as f:
    #     input_file = f.read()
    # assert main(input_file) == '542210', 'input3.txt error\n' + str(
    #     main(input_file))
