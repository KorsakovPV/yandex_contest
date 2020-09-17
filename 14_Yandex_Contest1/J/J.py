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


def solution(list_input, list_sample):
    answer = Counter(list_input)
    answer_keys = list(answer.keys())
    answer_str = ''
    for i in list_sample:
        answer_str += '{0} '.format(i) * answer[i]
        answer_keys.remove(i)
    answer_keys.sort()

    for i in answer_keys:
        answer_str += '{0} '.format(i) * answer[i]
    return answer_str.rstrip()


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    if n == 0:
        return ''
    list_input = list(map(int, input_file[1].split()))
    m = int(input_file[2])
    if m == 0:
        list_sample = list()
    else:
        list_sample = list(map(int, input_file[3].split()))
    sol = solution(list_input, list_sample)
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
        input_file) == '2 4 3 5 6 0 7 7 8 9', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '2 2 2 1 4 3 3 9 6 7 19', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '3 3 10 5 9 2 7 6 0 4 8', 'input3.txt error\n' + str(
        main(input_file))
