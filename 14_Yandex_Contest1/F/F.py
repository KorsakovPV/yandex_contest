"""
F. Сортировка по четности

Кондратий издал новый закон. Во всех списках четные числа должны стоять на
четных позициях, а нечетные числа - на нечетных. Уже существующие списки
придется пересортировать. В списках, которые вам достанутся, одинаковое
количество четных и нечетных элементов. Нужно отсортировать его в соответствии
с новым законом. Исходный порядок внутри групп четных и нечетных элементов
менять нельзя.

Формат ввода
В первой строке записано n - целое четное число в диапазоне от 0 до 10000 Далее
в строку через пробел записаны n чисел, каждое из которых не превосходит 10000

Формат вывода
Нужно вывести массив, отсортированный согласно условию.
"""


def solution(list_odd):
    answer = []
    odd1 = []
    odd2 = []
    for i in list_odd:
        if i % 2 == 0:
            odd2.append(i)
        else:
            odd1.append(i)

    i = 0
    while i < len(odd1):
        answer.append(odd2[i])
        answer.append(odd1[i])
        i += 1
    return answer


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    if n > 0:
        list_odd = list(map(int, input_file[1].rstrip().split()))
    else:
        return ''
    #     list_odd = ''
    sol = solution(list_odd)
    return ' '.join(map(str, sol))


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '4 5 2 7', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '6 1 2 1 4 5 4 5', 'input2.txt error\n' + str(
        main(input_file))

    # with open('input3.txt') as f:
    #     input_file = f.read()
    # assert main(input_file) == '2 6', 'input3.txt error\n' + str(
    #     main(input_file))
