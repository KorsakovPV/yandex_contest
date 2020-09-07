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

def rec_data(matrix, i, j, x, y, data_list):
    if i >= x or j >= y:
        return data_list
    for p in range(j, y):
        data_list.append(matrix[i][p])
    for p in range(i + 1, x):
        data_list.append(matrix[p][y - 1])
    if (x - 1) != i:
        for p in range(y - 2, j - 1, -1):
            data_list.append(matrix[x - 1][p])
    if (y - 1) != j:
        for p in range(x - 2, i, -1):
            data_list.append(matrix[p][j])
    return rec_data(matrix, i + 1, j + 1, x - 1, y - 1, data_list)

def сookies(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    m = int(s[1])
    arr = s[2:]
    array = []
    for i in arr:
        array.append(i.split())

    array_answer = rec_data(array, 0, 0, n, m, [])

    return '\n'.join(array_answer) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(сookies(input_file))


if __name__ == '__main__':
    input_txt = 'input1.txt'

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