"""
I. Одинаковые суммы

Гоше стало интересно, можно ли разбить все заработанные им во время игры в
Лампу очки на две части так, чтобы сумма в них была одинаковой.

Формат ввода
В первой строке записано число элементов массива n. Оно не превосходит 10000

Далее в строку записаны n целых неотрицательных чисел, каждое из которых не
превосходит 10000

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе — False
"""


# Жадное решение
def split(input_file):
    s = input_file.strip().split('\n')
    n = int(s[0])
    nums = [int(x) for x in s[1].split()]
    amount = sum(nums)
    if amount % 2 == 1:
        return False
    nums.sort(reverse=True)
    subsum = [0] * 2
    target = amount // 2
    n = len(nums)

    def dfs(i):
        if i == n:
            return True
        for j in range(2):
            subsum[j] += nums[i]
            if subsum[j] <= target and dfs(i + 1):
                return True
            subsum[j] -= nums[i]
            if subsum[j] == 0:
                break
        return False

    return dfs(0)


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(split(input_file)) + '\n'


if __name__ == '__main__':
    input_txt = 'input2.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == 'True\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == 'False\n', 'input2.txt error\n' + main(
        'input2.txt')
