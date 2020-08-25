"""
Перед Тимофеем стоит задача написать несколько реализаций собственной очереди,
так как доступные на рынке варианты для проекта не подходят. Требования к
первой вот такие: класс должен называться MyQueue(), поддерживать операции
добавления, удаления, получения элемента, определение текущего размера, и
метод, показывающий, пуста ли очередь или нет. Реализована структура данных
должна быть на основе массива.

Формат ввода
В первой строке записано одно число - количество команд, оно не превосходит
5000. Далее идут команды по одной в строке. Команды могут быть следующих видов:

push x - добавить число x в очередь

pop - удалить число из очереди и напечатать его

peek - напечатать первое число в очереди

size - вернуть размер очереди

Формат вывода
Для каждой команды size, peek и pop напечатайте результат её выполнения. Если
очередь пуста, для команды peek напечатайте None. Если происходит удаление из
пустой очереди — напечатайте None.
"""


class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size_queue = 0

    def isEmpty(self):
        return self.size_queue == 0

    def size(self):
        return self.size_queue

    def push(self, item):
        if self.size_queue < self.max_n:
            self.queue[self.tail] = item
            self.tail += 1
            self.size_queue += 1

    def pop(self):
        if self.isEmpty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size_queue -= 1
        return x

    def peek(self):
        if self.isEmpty():
            return 'None'
        return self.queue[self.head]


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()
n = int(input_file[0])
commands = input_file[1:]
queue = MyQueue(n)
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'push':
        queue.push(int(command[1]))
    elif command[0] == 'pop':
        output_file += str(queue.pop()) + '\n'
    elif command[0] == 'peek':
        output_file += str(queue.peek()) + '\n'
    elif command[0] == 'size':
        output_file += str(queue.size()) + '\n'

#print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
