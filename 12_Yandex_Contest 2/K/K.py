"""
K. Уникальный Стек

Реализуйте класс StackSet, который хранит только уникальные элементы. При этом
операция добавления элемента в стек должна выполняться за O(1).

Формат ввода
В первой строке записано одно число - количество команд. Далее идут команды по
одной на строке. Команды могут быть следующих видов:

push x - добавить число x в стек

pop - удалить число с вершины стека

peek - напечатать число с вершины стека (без удаления)

size - узнать размер стека

Если стек пуст при вызове команд pop и peak нужно вывести на печать error.

Формат вывода
Для каждой команды size напечатайте результат её выполнения. Если происходит
удаление из пустого стека - напечатайте error.
"""


class StackSet:
    def __init__(self):
        self.items = []
        self.items_set = set()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if item not in self.items_set:
            self.items.append(item)
            self.items_set.add(item)

    def pop(self):
        if len(self.items) > 0:
            self.items_set.remove(self.items[len(self.items) - 1])
            return self.items.pop()
        return 'error\n'

    def peek(self):
        if len(self.items) > 0:
            return str(self.items[len(self.items) - 1]) + '\n'
        return 'error\n'

    def size(self):
        return str(len(self.items)) + '\n'


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()
n = input_file[0]
commands = input_file[1:]
stack = StackSet()
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'peek':
        output_file += stack.peek()
    elif command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        if stack.isEmpty():
            output_file += 'error\n'
        else:
            stack.pop()
    elif command[0] == 'size':
        output_file += stack.size()

print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
