"""
K. Единицы

Пока Вася писал программу про степени четверки, погода на улице ухудшилась. Он
долго не расстраивался и придумал новую задачку! Ему нравится работать с
системами счисления. И вот что на этот раз получилось: Дано целое положительное
число. Нужно посчитать, сколько 1 встречается в двоичной записи этого числа.

Формат ввода
На вход подается число в диапазоне от 1 до 10000

Формат вывода
Выведите одно число - количество единиц.
"""

def dec_to_bin(num):
    values = '01'
    d, e = divmod(num, 2)
    if d >= 1:
        return dec_to_bin(d) + values[e]
    else:
        return values[e]


f = open('input.txt')
input_file = f.read()

output = str(dec_to_bin(int(input_file)))
output_counter = output.count('1')

f = open('output.txt', 'w')
f.write((str(output_counter)) + '\n')
f.close()
