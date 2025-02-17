"""
I. Стек - Max

Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс также должен поддерживать все
операции, реализованные в классе Stack, из урока. При этом в классе StackMax
может быть реализовано не более трёх методов.

Стек может содержать только данные типов, поддерживающих операцию сравнения.
Иначе операция поиска максимума будет некорректной.

Формат ввода
В первой строке записано одно число n - количество команд. n не превосходит
1000. В следующих n строках идут команды. Команды могут быть следующих видов:

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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return 'None\n'
        else:
            max_value = int(self.items[0])
            for i in self.items:
                if int(i) > int(max_value):
                    max_value = int(i)
            return str(max_value) + '\n'


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()
n = input_file[0]
commands = input_file[1:]
stack = Stack()
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'get_max':
        output_file += stack.get_max()
    elif command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        if stack.isEmpty():
            output_file += 'error\n'
        else:
            stack.pop()

# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
