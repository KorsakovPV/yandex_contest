"""
H. Возрастающий подмассив

Во сне Гоша долго играл в игру Лампочка. Он то выигрывал, то проигрывал. Ему
стало интересно, сколько максимум партий подряд он получал большее количество
очков, чем в предыдущей.

Формат ввода
В первой строке записано число элементов массива n. Оно не превосходит 100000

Далее в строку записаны n чисел, каждое из которых по модулю не превосходит
1000

Формат вывода
Нужно вывести одно число, равное длине наибольшего возрастающего подмассива

"""


def subarray(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    array = [int(x) for x in s[1].split()]
    count = 1
    count_max = 0
    for i in range(n-1):
        if array[i] < array[i+1]:
            count += 1
        else:
            if count_max < count:
                count_max = count
            count = 1
        if count_max < count:
            count_max = count

    return str(count_max) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(subarray(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main(
        'input1.txt') == '5\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main(
        'input2.txt') == '2\n', 'input2.txt error\n' + main(
        'input2.txt')
    assert main(
        'input3.txt') == '3\n', 'input3.txt error\n' + main(
        'input3.txt')
