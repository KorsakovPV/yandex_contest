"""
G. Закручивающаяся спираль

Волшебная фея отправила Гоше послание. Чтобы никто не смог перехватить
сообщение, фея его закодировала. Послание записано в матрице по спирали,
начиная с левого верхнего угла вправо. Помогите Гоше прочитать сообщение.

Формат ввода
В первой строке записано число n — количество строк матрицы

Во второй — m — количество столбцов

В следующих n строках записано по m чисел

Формат вывода
Нужно вывести на печать по спирали элементы матрицы: начиная с левого верхнего
угла вправо.


"""


def сookies(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    m = int(s[1])
    arr = s[2:]
    array = []
    array_answer = []
    index_n = 0
    index_m = 0
    for i in arr:
        array.append(i.split())
    move_direction = 'r'
    turn = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
    move = {'r': [0, 1],
            'd': [1, 0],
            'l': [0, -1],
            'u': [-1, 0]}

    if n == 1:
        return '\n'.join(array[0]) + '\n'

    if m == 1:
        answer = []
        for i in array:
            answer.append(i[0])
        return '\n'.join(answer) + '\n'

    while len(array_answer) < n * m:
        array_answer.append(array[index_n][index_m])
        array[index_n][index_m] = None
        if index_n + move[move_direction][0] >= n or index_m + move[move_direction][1] >= m or index_m + move[move_direction][1] < 0:
            move_direction = turn[move_direction]
        if array[index_n + move[move_direction][0]][index_m + move[move_direction][1]] is None:
            move_direction = turn[move_direction]
        index_n += move[move_direction][0]
        index_m += move[move_direction][1]

    return '\n'.join(array_answer) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(сookies(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main(
        'input1.txt') == '1\n2\n3\n4\n8\n12\n11\n10\n9\n5\n6\n7\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main(
        'input2.txt') == '-4\n3\n7\n-3\n6\n-5\n2\n2\n6\n-3\n-7\n9\n1\n-8\n-1\n', 'input2.txt error\n' + main(
        'input2.txt')
    assert main(
        'input3.txt') == '1\n2\n5\n6\n', 'input3.txt error\n' + main(
        'input3.txt')
    assert main(
        'input4.txt') == '1\n2\n5\n6\n', 'input4.txt error\n' + main(
        'input4.txt')
    assert main(
        'input5.txt') == '1\n', 'input5.txt error\n' + main(
        'input5.txt')