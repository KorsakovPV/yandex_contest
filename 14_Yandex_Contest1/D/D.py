"""
C. Эффективная быстрая сортировка

Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не должно
требоваться O(n) дополнительной памяти. А у вас получится?

Формат ввода
В первой строке на вход подается число n - длина массива. n не превосходит
1000. Во второй строке через пробел записаны n чисел. Каждое из чисел по модулю
не превосходит 1000.

Формат вывода
Нужно вывести через пробел числа в отсортированном по возрастанию порядке.
https://www.geeksforgeeks.org/python-program-for-quicksort/
"""


def quicksort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = list(map(int, input_file[1].rstrip().split()))
    sol = quicksort(data)
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
