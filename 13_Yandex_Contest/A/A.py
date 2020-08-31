"""
A. Расписание

Помогите Алле написать код алгоритма для выбора уроков, которые пройдут в
классе.
Дано расписание предметов. Нужно составить расписание, в соответствии с которым
в классе можно будет провести как можно больше уроков.

Формат ввода
В первой строке задано число предметов. Оно не превосходит 1000.
Далее для каждого предмета в отдельной строке записано время начала и окончания
урока. Обратите внимание на формат времени. Указываются только значащие цифры.

Формат вывода
Выведите информацию о всех уроках, которые нужно провести в кабинете, в порядке
возрастания времени начала.

Примечания
Если возможно несколько оптимальных вариантов, нужно выбирать урок, у которого
начало раньше.
Возможно проведение более чем одного урока нулевой длительности одновременно.
"""


class Stack:
    def __init__(self):
        self.lessons = []

    def is_empty(self):
        return self.lessons == []

    def push(self, lesson):
        self.lessons.append(lesson)

    def pop(self, lesson=None):
        if not self.is_empty():
            if lesson is None:
                return self.lessons.pop()
            elif 0 <= lesson and lesson < self.size():
                return self.lessons.pop(lesson)

    def size(self):
        return len(self.lessons)

    def peak(self, lesson):
        if not self.is_empty():
            if 0 <= lesson and lesson < self.size():
                return self.lessons[lesson]

    def sort(self, key='tail', reverse=False):
        if key == 'head':
            self.lessons = sorted(self.lessons, key=lambda x: x[0],
                                  reverse=reverse)
        elif key == 'tail':
            self.lessons = sorted(self.lessons, key=lambda x: x[1],
                                  reverse=reverse)

        elif key == 'duration':
            self.lessons = sorted(self.lessons, key=lambda x: x[2],
                                  reverse=reverse)


def calc(input_file):
    input_file = input_file.strip().split('\n')
    n = input_file[0]
    input_lessons = input_file[1:]

    input_lessons_stack = Stack()

    # Способ 1
    select_lessons_stack = Stack()
    for lesson in input_lessons:
        input_lessons_stack.push(
            [float(lesson.split()[0]), float(lesson.split()[1]),
             float(lesson.split()[1]) - float(lesson.split()[0]), lesson])

    input_lessons_stack.sort(key='head', reverse=False)
    input_lessons_stack.sort(key='tail', reverse=False)
    select_lessons_stack.push(input_lessons_stack.peak(0))

    for i in range(1, len(input_lessons_stack.lessons)):
        if select_lessons_stack.lessons[len(select_lessons_stack.lessons) - 1][
            1] <= input_lessons_stack.lessons[i][0]:
            select_lessons_stack.push(input_lessons_stack.peak(i))

    max_duration_stack = select_lessons_stack

    output_file = str(len(max_duration_stack.lessons)) + '\n'

    for i in max_duration_stack.lessons:
        output_file += i[3] + '\n'

    return output_file


def main(input_file):
    f = open(input_file)
    input_file = f.read()
    f.close()

    return str(calc(input_file))


if __name__ == '__main__':
    input_txt = 'input6.txt'

    f = open('output.txt', 'w')

    f.write(main(input_txt) + '\n')

    f.close()

    assert main(
        'input1.txt') == '3\n9 10\n10 11\n11 12\n', "input1.txt error\n" + main(
        'input1.txt')
    assert main(
        'input2.txt') == '2\n9 10\n11 12.25\n', "input2.txt error\n" + main(
        'input2.txt')
    assert main(
        'input3.txt') == '3\n7 14\n19 19\n22 23\n', "input3.txt error\n" + main(
        'input3.txt')
    assert main('input4.txt') == '1\n5 6\n', "input4.txt error\n" + main(
        'input4.txt')
    assert main('input5.txt') == '1\n10 13\n', "input5.txt error\n" + main(
        'input5.txt')
    assert main(
        'input6.txt') == '21\n0 2\n2 2\n2 3\n4 4\n4 4\n5 5\n8 8\n8 11\n12 12\n13 13\n13 13\n14 14\n14 14\n15 16\n16 17\n17 18\n19 19\n19 19\n20 20\n20 20\n20 21\n', "input6.txt error\n" + main(
        'input6.txt')
    assert main(
        'input7.txt') == '15\n1.1 2.3\n3.8 3.8\n5.4 6.9\n7.3 9.2\n10.2 11.2\n12.6 12.7\n13.5 14.1\n15 15.3\n15.3 15.4\n15.4 16.6\n16.7 17.2\n17.2 17.6\n18.4 18.7\n19.8 19.8\n19.8 20.6\n', "input7.txt error\n" + main(
        'input7.txt')
