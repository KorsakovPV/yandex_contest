"""
Q. Статистика

В метро Гоша обычно играет в мобильную игру «‎Черепашенька». Он долго собирал
 данные о том, сколько очков зарабатывает и проигрывает в день. Гоша собирает
 необычную статистику. Нужно определить максимальное произведение заработанных
 очков среди троек дней, в которые сумма очков равна нулю, и произведение
 является положительным числом.

Формат ввода
В первой строке записано число n (1 ≤ n ≤ 2000). В следующей строке через
пробел записаны n целых чисел. Числа находятся в диапазоне от -10000 до 10000.

Формат вывода
Выведите максимальное положительное произведение заработанных за три дня очков
среди троек дней, в которые их сумма равна нулю. Если троек, удовлетворяющих
условиям, нет, нужно вывести -1.
"""

from itertools import permutations, combinations

f = open('input.txt')
input_file = f.read().split()
n = int(input_file[0])
score_data = input_file[1:]
score_data.sort(key=None, reverse=True)
max_product = -1

for i in range(n-2): 
    score_amount = int(score_data[i])+int(score_data[i+1])+int(score_data[i+2])
    score_multiplication = int(score_data[i])*int(score_data[i+1])*int(score_data[i+2])
    if score_amount == 0 and score_multiplication > 0:
        max_product = score_multiplication


output_data = str(max_product)
print(output_data)
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()


