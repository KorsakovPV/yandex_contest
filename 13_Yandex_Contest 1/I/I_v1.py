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

#Перебор
def next_indexes_set(indexes, numCount):
    count = len(indexes)
    for reverseIndex in range(1, count + 1):
        if indexes[-reverseIndex] < (numCount - reverseIndex):
            indexes[-reverseIndex] += 1
            for index in range(count - reverseIndex + 1, count):
                indexes[index] = indexes[index - 1] + 1
            return True
    return False


def split_list(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    numbers = [int(x) for x in s[1].split()]
    numCount = n
    fullSum = sum(numbers)
    searchSum = fullSum // 2

    for count in range(numCount // 2 + 1, 1, -1):
        indexes = [i for i in range(count)]
        while 1:
            curSum = sum([numbers[i] for i in indexes])
            if curSum == searchSum:
                return 'True' + '\n'
            if not next_indexes_set(indexes, numCount):
                break
    return 'False' + '\n'


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
