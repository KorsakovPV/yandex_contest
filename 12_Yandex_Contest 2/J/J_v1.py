"""
J. Стек - MaxEffective

Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push и pop также
должны выполняться за константное время.

Формат ввода
В первой строке записано одно число - количество команд, оно не превосходит
100000. Далее идут команды по одной в строке. Команды могут быть следующих
видов:

push x - добавить число x в стек

pop - удалить число с вершины стека

get_max - напечатать максимальное число в стеке

Если стек пуст при вызове команды get_max нужно напечатать None, для команды
pop - error.

Формат вывода
Для каждой команды get_max напечатайте результат её выполнения. Если стек
пустой, для команды get_max напечатайте None. Если происходит удаление из
пустого стека - напечатайте error.
"""

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.max) == 0:
            self.max.append(item)
        elif self.max[len(self.max) - 1] > item:
            self.max.append(self.max[len(self.max) - 1])
        else:
            self.max.append(item)
        self.items.append(item)

    def pop(self):
        self.max.pop()
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return 'None\n'
        else:
            return str(self.max[len(self.max) - 1]) + '\n'


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()
n = input_file[0]
commands = input_file[1:]
stack = StackMaxEffective()
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'get_max':
        output_file += stack.get_max()
    elif command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        if stack.isEmpty():
            output_file += 'error\n'
        else:
            stack.pop()

print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
