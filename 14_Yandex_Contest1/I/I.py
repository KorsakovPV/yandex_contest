"""
I. Гардероб

Евлампия решила оставить у себя в гардеробе вещи только трех цветов: розового,
желтого, и малинового. Она захотела отсортировать одежду по цветам. Сначала
должны идти вещи розового цвета, далее - желтого, и в конце - малинового.
Помогите Евлампии навести порядок в гардеробе.

Формат ввода
В первой строке задано количество предметов в гардеробе: n - оно не превосходит
10000. Далее задан массив, в котором указан цвет для каждого предмета. Розовый
цвет обозначен 0, желтый - 1, малиновый - 2. Помогите Евлампии расположить
предметы в гардеробе так в соответствии с её задумкой.

Формат вывода
Нужно вывести в строку через пробел получившиеся предметы.
"""
from collections import Counter


def solution(list_flowerbed):
    answer = Counter(list_flowerbed)
    answer_str = '0 ' * answer[0] + '1 ' * answer[1] + '2 ' * answer[2]
    return answer_str.rstrip()


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    if n == 0:
        return ''
    list_flowerbed = list(map(int, input_file[1].split()))

    sol = solution(list_flowerbed)
    return str(sol)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '0 0 0 1 1 2 2', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '0 1 1 2 2', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '0 1 1 2 2 2', 'input3.txt error\n' + str(
        main(input_file))
