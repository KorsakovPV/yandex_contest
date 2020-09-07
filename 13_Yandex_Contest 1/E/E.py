"""
E. Печеньки

К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. У каждого ребёнка
есть фактор жадности — минимальный размер печенья, которое он возьмёт. Нужно
выяснить, сколько ребят останутся довольными.

Каждый ребёнок может взять не больше одного печенья.

Формат ввода
В первой строке записано n - количество детей.

Во второй - n чисел, разделенных пробелом - фактор жадности для каждого
ребенка, целое число, не превосходящее 1000.

В следующей строке записано - m - количество печенек.

Далее - m чисел, разделенных пробелом - размеры печенек.

Оба числа n и m не превосходят 10000.

Формат вывода
Нужно вывести одно число — количество детей, которые останутся довольными
"""


def сookies(input_file):
    s = input_file.strip().split('\n')
    n = s[0]
    greed = [int(x) for x in s[1].split()]
    quantity_сook = int(s[2])
    size_cook = [int(x) for x in s[3].split()]
    greed.sort()
    size_cook.sort()

    index_cook = 0
    index_greed = 0
    happy_greed = 0
    while index_cook < len(size_cook) and index_greed < len(greed):
        if greed[index_greed] <= size_cook[index_cook]:
            index_cook += 1
            index_greed += 1
            happy_greed += 1
        else:
            index_cook += 1

    return str(happy_greed) + '\n'


def main(input_file):
    with open(input_file) as f:
        input_file = f.read()

    return str(сookies(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    f.close()

    assert main('input1.txt') == '2\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1\n', 'input2.txt error\n' + main(
        'input2.txt')
