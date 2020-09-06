"""
K. Ипотека

Дочь Кондратия Евлампия решила купить в ипотеку несколько домов на территории
Трешландии.

Она нашла n объявлений о продаже. Известна стоимость каждого дома в
трешландских франках. Евлампия может позволить себе взять ипотеку на общую
сумму k франков. Нужно помочь ей определить, какое наибольшее количество домов
можно купить на эти деньги.

Формат ввода
В первой строке через пробел записаны целые числа n и k

n - количество домов, которые рассматривает Евлампия, оно не превосходит 1000

k - общий бюджет, не превосходит 10000

В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не
превосходит 10000. Все стоимости - целые числа.

Формат вывода
Выведите число, равное максимально возможному числу домов, которые может купить
Евлампия


"""


def calc(input_file):
    s = input_file.strip().split()
    n = int(s[0])
    k = int(s[1])
    home_value_array = [int(x) for x in s[2:]]
    home_value_array.sort()
    count = 0
    count_value = 0
    for home_value in home_value_array:
        if k - count_value > home_value:
            if n == 0:
                break
            n -= 1
            count += 1
            count_value += home_value

    return str(count) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(calc(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == '0\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '2\n', 'input2.txt error\n' + main(
        'input2.txt')
