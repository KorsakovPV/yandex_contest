"""
I. Двоичная система

Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной
системе счисления. Он ответил, что проходил это на одной из первых лекций по
информатике. Тимофей предложил Саше решить задачку. Два числа записаны в
двоичной системе счисления. Нужно вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел
применять нельзя.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.

Формат вывода
Одно число в двоичной системе счисления.
"""

f = open('input.txt')
input_file = f.read()
f.close()
augend1, augend2 = input_file.split()

augend1 = int(augend1, base=2)
augend2 = int(augend2, base=2)
output_data = bin(augend1 + augend2)[2:]
"""
augend1 = [*augend1[::-1]]
augend2 = [*augend2[::-1]]
amount = []

n = max(len(augend1), len(augend2))

for i in range(n):
    if len(amount) <= i:
        amount.append('0')
    if len(augend1) <= i:
        augend1.append('0')
    if len(augend2) <= i:
        augend2.append('0')
    amount_i = int(augend1[i]) + int(augend2[i]) + int(amount[i])
    if amount_i == 0:
        amount[i] = '0'
    elif amount_i == 1:
        amount[i] = '1'
    elif amount_i == 2:
        amount[i] = '0'
        amount.append('1')
    elif amount_i == 3:
        amount[i] = '1'
        amount.append('1')
output_data = ''.join(amount)[::-1]"""

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
