"""
N. Ограниченная очередь

Далее Тимофею нужно написать класс MyQueueSized(), который принимает параметр
max_size, означающий максимально допустимое количество элементов в очереди.

Формат ввода
В первой строке записано одно число - количество команд, оно не превосходит
5000. Во второй строке задан максимально допустимый размер очереди, он не
превосходит 5000. Далее идут команды по одной на строке. Команды могут быть
следующих видов:

push x - добавить число x в очередь

pop - удалить число из очереди и вывести на печать

peek - напечатать первое число в очереди

size - вернуть размер очереди

При превышении допустимого размера очереди нужно вывести "error". При вызове
операции pop для пустой очереди нужно вернуть None.

Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""


class MyQueueSized:
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
            self.tail = (self.tail + 1) % self.max_n
            self.size_queue += 1
            return ''
        else:
            return 'error\n'

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
count_commands = int(input_file[0])
queue_size = int(input_file[1])
commands = input_file[2:]
queue = MyQueueSized(queue_size)
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'push':
        output_file += str(queue.push(int(command[1])))
    elif command[0] == 'pop':
        output_file += str(queue.pop()) + '\n'
    elif command[0] == 'peek':
        output_file += str(queue.peek()) + '\n'
    elif command[0] == 'size':
        output_file += str(queue.size()) + '\n'

# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
