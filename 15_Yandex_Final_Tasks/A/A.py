"""
A. Кондратиева пирамида

В Трешландии проводились ежегодные соревнования по заезду на барсучьих
упряжках. Нужно обработать результаты забегов. Данные представлены в формате:
имя участника - список заработанных очков
Нужно отсортировать данные по такому принципу:
Если сумма набранных очков участника A больше, чем у участника В, то А должен
идти в списке раньше. При подсчете суммы нужно учитывать только положительные
значения очков.
Если суммы равны, то первым должен идти участник, чье имя лексикографически
меньше.
При совпадении имен раньше должен идти участник, который во входных данных
находится позже.
При этом, если из имени участника можно составить английский вариант имени
Кондратий (например, если имя nekondratiy или drkonxxxiyatt), то все правила
отменяются. Он должен идти в списке раньше. Если таких участников больше
одного, то раньше должен идти тот, кто находится позже во входных данных.
(Заработанные очки не рассматриваются).

Формат ввода
В первой строке задано n - число участников. Оно не превосходит 10000. В
следующих n строках записана информация о каждом из участников в обозначенном
формате. Имя состоит из строчных латинских букв. Длина имени не превосходит
100.
Длина списка набранных очков не больше 1000. Каждое из очков по модулю не
превосходит 1000.

Формат вывода
Нужно вывести данные в отсортированном порядке в таком же формате.

Пример 1
Ввод
3
anna 1 -4 5 0 1
sam 1 9 5 0 1
kondratiy 1 9 5 0 -1
kondratiy 1 9 5 0 -1

Вывод
sam 1 9 5 0 1
anna 1 -4 5 0 1
Пример 2

Ввод
2
anna 1 -4 5 0 1
sam 1 -4 5 0 1

Вывод
anna 1 -4 5 0 1
sam 1 -4 5 0 1
Примечания
Нужно реализовать алгоритм пирамидальной сортировки.
"""
import heapq


def amount_point(points):
    answer_amount = 0
    for point in points:
        if point > 0:
            answer_amount += point
    return answer_amount


def detect_kondratiy(name):
    return set('kondratiy') <= set(name)


def main(input_str):
    input_str = input_str.rstrip().split('\n')
    n = int(input_str[0])
    riders1 = list()
    riders2 = list()
    for i in range(1, n + 1):
        temp = input_str[i].split()
        name = temp[0]
        points = list(map(int, temp[1:]))
        if detect_kondratiy(name):
            riders1.append(
                [-amount_point(points), name, - i, input_str[i]])
        else:
            heapq.heappush(riders2,
                           [-amount_point(points), name, - i, input_str[i]])
    answer_str = ''
    for i in riders1:
        answer_str += i[3] + '\n'
    while len(riders2) > 0:
        answer_str += heapq.heappop(riders2)[3] + '\n'
    return answer_str


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == 'kondratiy 1 9 5 0 -1\nsam 1 9 5 0 1\nanna 1 -4 5 0 1\n', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == 'anna 1 -4 5 0 1\nsam 1 -4 5 0 1\n', 'input2.txt error\n' + str(
        main(input_file))
