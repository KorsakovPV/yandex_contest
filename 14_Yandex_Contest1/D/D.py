"""
D. Тараканьи бега

Сегодня 31 апреля, и в Удотинске по традиции проводятся тараканьи бега. Забеги
разделены на две категории. Если таракан участвовал в забеге одной из
категорий, он не может принимать участие в забегах другой категории. Но
встречаются нарушители! Помогите судьям их выявить и восстановить
справедливость.

Есть два списка со стартовыми номерами тараканов. Нужно вывести номера, которые
встречаются и в первом, и во втором списке. Квадратичный алгоритм не подойдет
для этой задачи. Тараканы разбегутся, пока алгоритм закончит работу.

Формат ввода
В первой строке записано число n - длина первого списка. Во второй строке -
число m - длина второго списка. Оба числа не превосходят 10000 В следующих двух
строках через пробел могут быть записаны два списка соответствующей длины,
состоящие из чисел, не превосходящих 10000.

Формат вывода
Нужно в строку вывести стартовые номера тараканов в порядке, в котором они
встречались в первом списке.
"""


def solution(list_cockroach1, list_cockroach2):
    set_cockroach1 = set(list_cockroach1)
    set_cockroach2 = set(list_cockroach2)
    answer = []
    for i in list_cockroach1:
        if i in set_cockroach1:
            set_cockroach1.remove(i)
            if i in list_cockroach2:
                answer.append(i)
    return answer


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])  # длинна первого списка
    m = int(input_file[1])  # длинна второго списка
    if n > 0:
        list_cockroach1 = list(map(int, input_file[2].rstrip().split()))
    else:
        return ''
        list_cockroach1 = []
    if m > 0:
        list_cockroach2 = list(map(int, input_file[3].rstrip().split()))
    else:
        list_cockroach2 = []
    sol = solution(list_cockroach1, list_cockroach2)
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
        input_file) == '4 9', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == '7', 'input2.txt error\n' + str(
        main(input_file))

    # with open('input3.txt') as f:
    #     input_file = f.read()
    # assert main(input_file) == '542210', 'input3.txt error\n' + str(
    #     main(input_file))
