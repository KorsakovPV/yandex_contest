"""
D. Соседи

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его
соседей. Соседним считается элемент, находящийся от текущего на одну ячейку
влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A:


соседними элементами для (0, 0) будут 2 и 0 А для (2, 1) — 1, 2, 7, 7.

Формат ввода
В первой строке задано n - количество строк матрицы. Во втрой - m - количество
столбцов. Числа m и n не превосходят 1000. В следующих n строках задана
матрица. Элементы матрицы - целые числа, по модулю не превосходящие 1000. В
последних двух строках записаны координаты элемента (индексация начинается с
нуля), соседей которого нужно найти.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
"""


def func(input_file):
    n, m, input_data, nt, mt = int(input_file[0]), int(input_file[1]), input_file[2:-2], int(input_file[-2]), int(input_file[-1])

    data = [input_data[i:i + m] for i in range(0, len(input_data), m)]

    neighbors = list()

    if 0 <= nt + 1 <= n - 1 and 0 <= mt <= m - 1:
        neighbors.append((data[nt + 1][mt]))
    if 0 <= nt - 1 <= n - 1 and 0 <= mt <= m - 1:
        neighbors.append((data[nt - 1][mt]))
    if 0 <= nt <= n - 1 and 0 <= mt + 1 <= m - 1:
        neighbors.append((data[nt][mt + 1]))
    if 0 <= nt <= n - 1 and 0 <= mt - 1 <= m - 1:
        neighbors.append((data[nt][mt - 1]))

    neighbors.sort(key=int)

    return ' '.join(neighbors)


f = open('input.txt')
input_file = f.read().rstrip()
f.close()

output_file = func(input_file.split())
# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
