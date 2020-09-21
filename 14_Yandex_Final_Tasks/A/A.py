"""
A. Большое число

Вечером ребята решили поиграть в игру "Большое число".
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n - количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно из них составить.
"""


# 34601917
class solution_key(str):
    def __lt__(self, y):
        return self + y > y + self

class Solution:
    def largest_number(self, nums):
        nums.sort(key=solution_key)
        return ''.join(nums)

def main(input_file):
    input_file = input_file.rstrip().split('\n')
    data = input_file[1].rstrip().split()
    sol = Solution()
    return sol.largest_number(data)


def test(num):
    left = 1
    while left < len(num) // 2:
        data = list()
        data.append(num[:left])
        data.append(num[left:-left])
        data.append(num[-left:])
        sol = Solution()
        print(data, sol.largest_number(data))
        left += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    # test('123456789')
    # test('998877665544332211')
    # test('11111111112')

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(input_file) == '56215', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(input_file) == '78321', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '542210', 'input3.txt error\n' + str(
        main(input_file))
