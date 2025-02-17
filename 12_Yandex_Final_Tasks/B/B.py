"""
B. Циклы

В этом спринте вы изучили структуру данных Связный список.
В Связном списке можно, например, хранить дни недели. Вторник за понедельником,
 среда за вторником, и так далее.
PIC

Вам предстоит это выяснить!
В качестве второго задания финального проекта нужно написать программу, которая
определяет, есть ли цикл в связном списке.
На вход функция принимает голову списка, на выходе должна выдать True, если в
списке содержится цикл, иначе — False. Размер дополнительной памяти, к которой
обращается функция, не должен превышать О(1).

Формат ввода
В этой задаче вам нужно реализовать только функцию с решением, считывать
входные данные не нужно.
Функция должна принимать на вход голову связного списка.
Класс, представляющая узел списка выглядит так:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return self.value
Ваша функция должна называться hasCycle.
Формат вывода
Функция должна возвращать булево значение
Примечания
При отправке нужно выбирать компилятор make и загружать решение в виде файла.
Файл может быть назван любым именем, кроме solution.py
Расширение .py должно присутствовать обязательно.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return self.value

def hasCycle(node):
    if type(node) != Node:
        return

    if node.next is None:
        return False

    iter_step1 = iter_step2 = node
    while iter_step2 is not None and iter_step2.next is not None:
        iter_step1 = iter_step1.next
        iter_step2 = iter_step2.next.next

        if iter_step1 == iter_step2:
            return True
    return False

if __name__ == '__main__':
    nnn = []

    nnn.append(Node('last'))

    for i in range(10):
        nnn.append(Node(str(i), nnn[i]))

    nnn[0].next = nnn[len(nnn)-1]



    print(hasCycle([]))
    print(hasCycle(Node('lasttttt')))
    print(hasCycle(nnn[len(nnn)-1]))
