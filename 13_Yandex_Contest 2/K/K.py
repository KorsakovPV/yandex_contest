"""
K. Корень из двух

В Трешландии своеобразная финансовая система. Из математических операций
используются не только стандартные: +, -, *, / Но также квадратный корень и
логарифм. Так что порой бывает сложно посчитать сдачу в магазине.
Феликс и Бенедикт, юные жители Удотинска, пошли в магазин купить капустное
мороженное. Но у кассира бобры сгрызли счеты. Помогите ребятам узнать, сколько
им должны дать сдачи. Напишите функцию, вычисляющую квадратный корень из двух.

Формат вывода
Выведите значение квадратного корня из двух с точностью 5 знаков после запятой

Примечания
Функцией, вычисляющей корень, из стандартной библиотеки пользоваться нельзя.
"""


def solution_sqrt(n):
    n_sqrt = float(n)
    step = n_sqrt / 2
    count = 0
    while round(n_sqrt * n_sqrt, 5) != n:
        count += 1
        if n_sqrt * n_sqrt > n:
            n_sqrt -= step
            step /= 2
        else:
            n_sqrt += step
            step /= 2
    return round(n_sqrt, 5)


if __name__ == '__main__':
    print(solution_sqrt(2))

    # assert main(
    #     'input1.txt') == '0', 'input1.txt error\n' + str(main(
    #     'input1.txt'))
    # assert main('input2.txt') == '1', 'input2.txt error\n' + str(main(
    #     'input2.txt'))
