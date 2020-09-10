"""
L. Банкомат

Тимофей пошел снять деньги в банкомат. Ему нужно n трешландийских долларов. В
банкомате в бесконечном количестве имеется n монет различных достоинств. Нужно
определить число способов, которыми Тимофей сможет набрать нужную сумму.

Формат ввода
В первой строке записано m - сумма, которую нужно набрать. Во второй строке
n - количество монет в банкомате. Оба числа не превосходят 300. Далее в строку
записано n чисел, каждое в диапазоне от 1 до 1000.

Формат вывода
Нужно вывести число способов, которым Тимофей сможет набрать нужную сумму.

Примечания
В первом примере возможны следующие варианты:
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 3
1 + 2 + 2
2 + 3

Во втором примере всего две возможности набрать в сумме 3:
1 + 2
1 + 1 + 1

В третьем примере есть всего один номинал, которым мы не можем набрать нужную
сумму.
https://leetcode.com/problems/coin-change-2/
"""


def solution(m_amount, coins):
    amount_plus_1 = m_amount + 1
    solutions = [0] * amount_plus_1
    solutions[0] = 1
    for coin in coins:
        for j in range(coin, amount_plus_1):
            solutions[j] += solutions[j - coin]
    return solutions[-1]


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    m_amount = int(input_file[0])
    n = int(input_file[1])
    coins = list(map(int, input_file[2].split()))
    return solution(m_amount, coins)


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))

    assert main('input1.txt') == 5, 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == 2, 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == 0, 'input3.txt error\n' + str(
        main('input3.txt'))
