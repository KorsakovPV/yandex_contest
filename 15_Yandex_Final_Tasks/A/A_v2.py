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

Примечания
Нужно реализовать алгоритм пирамидальной сортировки.
"""
# 35144179
import heapq


class participant_of_race:
    def __init__(self,
                 index_number,
                 amount_positive_point,
                 name,
                 text_value,
                 detect_kondratiy):
        self.amount_positive_point = amount_positive_point
        self.name = name
        self.index_number = index_number
        self.text_value = text_value
        self.detect_kondratiy = detect_kondratiy

    @classmethod
    def from_string(cls, index_number, riders_name_point_str):
        temp = riders_name_point_str.split()
        amount_positive_point = sum(
            i for i in list(map(int, temp[1:])) if i > 0)
        name = temp[0]
        index_number = index_number
        text_value = riders_name_point_str
        detect_kondratiy = set('kondratiy') <= set(name)
        data = cls(index_number,
                   amount_positive_point,
                   name,
                   text_value,
                   detect_kondratiy)
        return data

    def __str__(self):
        return self.text_value

    def __lt__(self, other):
        if self.amount_positive_point > other.amount_positive_point:
            return True
        if self.amount_positive_point == other.amount_positive_point:
            if self.name < other.name:
                return True
            if self.name == other.name:
                if self.index_number > other.index_number:
                    return True


def sorting_riders(riders_list):
    riders1 = list()
    riders2 = list()
    while len(riders_list) > 0:
        item = riders_list.pop()
        if item.detect_kondratiy:
            riders1.append(item)
        else:
            heapq.heappush(riders2, item)
    for _ in range(len(riders2)):
        riders1.append(heapq.heappop(riders2))
    return riders1


def test():
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

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == 'kondratiy 1 9 5 0 1\nnamekondratiyqq -1 -4 -5 -1\nnamekondratiyqq -1 -4 -5 -1\naname 1 9 5 0 1\nzaname 1 9 5 0 1\nname 1 -4 5 0 1\nname 1 -4 5 0 1\n', 'input3.txt error\n' + str(
        main(input_file))

    with open('input4.txt') as f:
        input_file = f.read()
    assert main(
        input_file) == 'name 5 0\nname 2 3\nname 5 -4\nname 4 1\nname 5\n', 'input4.txt error\n' + str(
        main(input_file))


def main(input_str):
    input_str = input_str.rstrip().split('\n')
    riders_list = list()
    for i, item in enumerate(input_str[1:]):
        riders_list.append(participant_of_race.from_string(i, item))
    answer_str = ''
    for item in sorting_riders(riders_list):
        answer_str += str(item) + '\n'
    return answer_str


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    test()
