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

f = open('input.txt')
input_file = f.read().split()

score_data = list(map(int, input_file[1:]))

score_data.sort()

max_product = -1

for i1 in range(len(score_data) - 2):
    left = i1 + 1
    right = len(score_data) - 1
    while left < right:
        sum = score_data[i1] + score_data[left] + score_data[right]
        if sum == 0 and score_data[i1] * score_data[left] * score_data[
            right] > max_product:
            max_product = score_data[i1] * score_data[left] * score_data[right]
        if sum > 0:
            right -= 1
        else:
            left += 1

output_data = str(max_product)
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
