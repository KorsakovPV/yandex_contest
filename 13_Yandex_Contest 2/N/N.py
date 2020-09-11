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
import timeit


def solution5(a, b):
    pass


def solution5(num1, num2, nod=None):
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


def solution3(a, b, nod):  # Test 4 TL
    x0 = int(nod / a)
    if x0 < 0:
        step = 1
    else:
        step = -1
    stop_plus = True
    stop_minus = True
    x = 0
    min_sum_p = min_sum_m = 10000
    answer_plus = answer_minus = [10000, 10000]

    x = x0
    x_increment = 0
    while stop_plus or stop_minus:
        if stop_plus:
            x = x0 + x_increment
            y = (nod - a * x) / b
            if int(y) == y:
                if min_sum_p > abs(x) + abs(y):
                    min_sum_p = abs(x) + abs(y)
                    answer_plus = [x, int(y)]
                    stop_plus = False
                # else:
                #     stop_plus = False
        if stop_minus:
            x = x0 - x_increment
            y = (nod - a * x) / b
            if int(y) == y:
                if min_sum_m > abs(x) + abs(y):
                    min_sum_m = abs(x) + abs(y)
                    answer_minus = [x, int(y)]
                    stop_minus = False
                # else:
                # stop_minus = False
        x_increment += 1

    if abs(answer_plus[0]) + abs(answer_plus[1]) < abs(answer_minus[0]) + abs(
            answer_minus[1]):
        answer = answer_plus
    else:
        answer = answer_minus

    # answer.sort()
    return '{0} {1} {2}'.format(answer[0], answer[1], nod)


def solution2(a, b, nod):  # Test 21 TL
    # a, b = b, a
    stop_plus = True
    stop_minus = True
    x = 0
    min_sum = 10000
    answer_plus = answer_minus = [10000, 10000]
    while stop_plus or stop_minus:
        y = (nod - a * x) / b
        if int(y) == y:
            if min_sum > abs(x) + abs(y):
                min_sum = abs(x) + abs(y)
                answer_plus = [x, int(y)]
            else:
                stop_plus = False
        y = (nod + a * x) / b
        if int(y) == y:
            if min_sum > abs(x) + abs(y):
                min_sum = abs(x) + abs(y)
                answer_minus = [-x, int(y)]
            else:
                stop_minus = False
        x += 1

    if abs(answer_plus[0]) + abs(answer_plus[1]) < abs(answer_minus[0]) + abs(
            answer_minus[1]):
        answer = answer_plus
    else:
        answer = answer_minus

    # answer.sort()
    return '{0} {1} {2}'.format(answer[0], answer[1], nod)


def solution(a, b, nod):  # Test 10 TL
    y0 = nod / b
    x0 = nod / a
    x = 0
    stop_plus = True
    stop_minus = True
    if round(y0) == y0:
        min_sum = abs(y0)
        min_sum_previous = min_sum
        answer = [0, int(y0)]
    else:
        min_sum = a * b
        min_sum_previous = min_sum

    while stop_plus or stop_minus:
        x += 1
        y_plus = (nod - a * x) / b
        y_minus = (nod + a * x) / b
        if round(y_plus) == y_plus:
            if min_sum_previous < abs(y_plus) + abs(x):
                stop_plus = False
            if abs(y_plus) + abs(x) < min_sum:
                answer = [x, int(y_plus)]
                min_sum_previous = min_sum
                min_sum = abs(y_plus) + abs(x)
        if round(y_minus) == y_minus:
            if min_sum_previous < abs(y_minus) + abs(x):
                stop_minus = False
            if abs(y_minus) + abs(x) < min_sum:
                answer = [-x, int(y_minus)]
                min_sum_previous = min_sum
                min_sum = abs(y_minus) + abs(x)
    # answer.sort()
    return '{0} {1} {2}'.format(answer[0], answer[1], nod)


def solution_nod(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    a = int(input_file[0])
    b = int(input_file[1])
    nod = solution_nod(a, b)
    sol2 = solution4(a, b, nod)
    # sol2 = solution5(a, b, nod)
    return '{0} {1} {2}'.format(sol2[1], sol2[2], sol2[0])

if __name__ == '__main__':
    input_txt = 'input1.txt'

    a = timeit.default_timer()
    # codes
    for i in range(100000):
        x = main(input_txt)
    print(timeit.default_timer() - a)
    with open('output.txt', 'w') as f:
        f.write(str(x))

    assert main('input1.txt') == '-1 1 4', 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == '0 1 5', 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == '-2 1 1', 'input3.txt error\n' + str(
        main('input3.txt'))
    assert main('input4.txt') == '1 -8 3', 'input3.txt error\n' + str(
        main('input4.txt'))
