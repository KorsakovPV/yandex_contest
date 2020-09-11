"""
N. Безупречные коэффициенты

По дороге в Удотинск ребятам встретилось поле, на котором местные жители
выращивали подорожники. Поле разделено на одинаковые квадраты. Размер квадратов
вычислялся по алгоритму, который использовал Овощеслав для схожей задачи.
Тимофей рассказал друзьям, что, если размер участка равен a на b, можно найти
такие целые числа x и y, что они, будучи умноженными на a и b, в сумме дадут
наибольший общий делитель a и b.
Помогите ребятам по двум числам найти их НОД и коэффициенты его разложения в
линейную комбинацию через эти числа.

Формат ввода
В первой строке записана ширина участка, во второй - длина. Оба числа не
превосходят 10000.

Формат вывода
Выведите в строку через пробел 3 числа: коэффициент для a, коэффициент для b в
разложении НОД в линейную комбинацию через a и b, и сам НОД.

Примечания
Если a и b равны, то коэффициенты нужно выводить в отсортированном порядке.
Нужно выводить минимальную по модулю пару таких коэффициентов.
"""


def solution5(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = solution5(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)


def solution4(a, b, nod):  # Test 4 TL
    x0 = int(nod / a)
    y = (nod - a * x0) / b
    x = x0
    while int(y) != y:
        x += 1
        y = (nod - a * x) / b
    answer_plus = [x, int(y)]
    x = x0
    y = 0.1
    while int(y) != y:
        x -= 1
        y = (nod - a * x) / b
    answer_minus = [x, int(y)]

    if abs(answer_plus[0]) + abs(answer_plus[1]) < abs(answer_minus[0]) + abs(
            answer_minus[1]):
        answer = answer_plus
    else:
        answer = answer_minus
    return '{0} {1} {2}'.format(answer[0], answer[1], nod)


def solution_nod(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def test():
    from random import randrange
    print(10)
    for i in range(1000):
        a = 50#randrange(10000) + 1
        b = 50#randrange(10000) + 1
        str1 = solution4(a, b, solution_nod(a, b))
        sol2 = solution5(a, b)
        if a == b:
            str2 = '{1} {0} {2}'.format(sol2[1], sol2[2], sol2[0])
        else:
            str2 = '{0} {1} {2}'.format(sol2[1], sol2[2], sol2[0])
        if str1 != str2:
            print(a, b, solution_nod(a, b))
            print(str1)
            print(str2)
            break


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    a = int(input_file[0])
    b = int(input_file[1])
    sol2 = solution5(a, b)
    if a == b:
        return '{1} {0} {2}'.format(sol2[1], sol2[2], sol2[0])
    return '{0} {1} {2}'.format(sol2[1], sol2[2], sol2[0])


if __name__ == '__main__':
    input_txt = 'input1.txt'
    x = main(input_txt)
    with open('output.txt', 'w') as f:
        f.write(str(x))

    test()

    assert main('input1.txt') == '-1 1 4', 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == '0 1 5', 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == '-2 1 1', 'input3.txt error\n' + str(
        main('input3.txt'))
    assert main('input4.txt') == '1 -8 3', 'input4.txt error\n' + str(
        main('input4.txt'))

    assert main('input5.txt') == '69 -88 2', 'input5.txt error\n' + str(
        main('input5.txt'))
    assert main('input6.txt') == '1 -8 3', 'input6.txt error\n' + str(
        main('input6.txt'))
    assert main('input7.txt') == '1 -8 3', 'input7.txt error\n' + str(
        main('input7.txt'))
    assert main('input8.txt') == '1 -8 3', 'input8.txt error\n' + str(
        main('input8.txt'))
    assert main('input9.txt') == '1 -8 3', 'input9.txt error\n' + str(
        main('input9.txt'))
