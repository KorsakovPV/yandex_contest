"""
I. Призы

В конкурсе на самую быструю программу сортировки одинаковый результат получили
k человек. В призовом фонде имеется n монет различного достоинства. Нужно
определить, можно ли разделить их между победителями таким образом, чтобы
каждый получил одинаковую сумму.

Формат ввода
В первой строке задано k - количество победителей - целое число от 1 до 16. Во
второй строке задано n - количество монет - целое число, не превосходящее 16.
Далее в строку через пробел записано n чисел, каждое из которых не превосходит
10000.

Формат вывода
Нужно вывести True, если возможно разделить призовой фонд на равные части между
победителями, иначе - False.

"""


def alphabet(k, n, coins):
    coins.sort()
    amount = sum(coins)
    some_coins = amount / k
    if amount % k != 0 or coins[len(coins)] > some_coins:
        return False
    left = 0
    right = len(coins) - 1
    while left < right:
        if coins[right] == some_coins:
            n -= 1
            right -= 1
        if coins[left] + coins[right] == some_coins:
            left += 1
            right -= 1
            n -= 1
    return True


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    k = int(input_file[0])
    n = int(input_file[1])
    # coins = input_file[2].split()
    coins = list(map(int, input_file[2].split()))
    return alphabet(k, n, coins)


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))

    assert main(
        'input1.txt') == True, 'input1.txt error\n' + str(main(
        'input1.txt'))
    assert main('input2.txt') == False, 'input2.txt error\n' + str(main(
        'input2.txt'))
