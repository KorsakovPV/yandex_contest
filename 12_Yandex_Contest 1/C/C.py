"""
C. Списочная форма

Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма — это массив его цифр слева
направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход подается
количество цифр числа Х, списочная форма неотрицательного числа Х и число K.
Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке - длина списочной формы числа X. На следующей строке - сама
списочная форма с цифрами записанными через пробел. В последней строке записано
число K.

Формат вывода
Выведите списочную форму числа X+K.
"""

f = open('input.txt')
input_file = f.read()
f.close()
input_string = input_file.split()
len_list_form, list_form, k = int(input_string[0]), input_string[1:-1], int(input_string[-1])
output = 0
for i in range(len_list_form):
    output += 10 ** (len_list_form - i - 1) * int(list_form[i])
output += k
output = str(output)
output_file = ''
for i in output:
    output_file += i + ' '

f = open('output.txt', 'w')
f.write(str(output_file) + '\n')
f.close()
