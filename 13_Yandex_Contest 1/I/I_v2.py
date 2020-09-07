"""
I. Одинаковые суммы

Гоше стало интересно, можно ли разбить все заработанные им во время игры в
Лампу очки на две части так, чтобы сумма в них была одинаковой.

Формат ввода
В первой строке записано число элементов массива n. Оно не превосходит 10000

Далее в строку записаны n целых неотрицательных чисел, каждое из которых не
превосходит 10000

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе — False
"""


def gen_left(numbers):
    K = sum(numbers)
    prev = [-1] * (K // 2 + 1)
    prev[0] = 0
    for val in numbers:
        for i in range(K // 2, val-1, -1): # K//2..val inclusive
            if prev[i] == -1 and prev[i - val] != -1:
                prev[i] = val
    if prev[K//2] == -1:
        raise ValueError
    curr = K // 2
    while curr > 0:
        yield prev[curr]
        curr -= prev[curr]

def partition_equal_sums(numbers):
    left = list(gen_left(numbers))
    right = list(numbers)
    for item in left: # O(n**2)
        right.remove(item)
    if sum(right) != sum(left):
        return 'False\n'
    else:
        return 'True\n'

def split_list(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    numbers = list(map(int, s[1].split()))
    return partition_equal_sums(numbers)


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(split_list(input_file))


if __name__ == '__main__':
    input_txt = 'input3.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == 'True\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == 'False\n', 'input2.txt error\n' + main(
        'input2.txt')
