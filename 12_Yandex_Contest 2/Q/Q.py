"""
Q. Дек

Гоша решил реализовать структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back, push_front, pop_front, pop_back
работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите
Гоше! Напишите эффективную реализацию.

Формат ввода
В первой строке записано количество команд n - целое число, не превосходящее
5000. Во второй строке записано число m - максимальный размер дека. Он не
превосходит 1000. В следующих n строках записана одна из команд:
push_back value
push_front value
pop_front
pop_back
value - целое число, по модулю не превосходящее 1000.

Формат вывода
При вызове команд pop_front и pop_back нужно вывести возвращаемое значение.
Если они вызываются для пустого дека — напечатайте 'error'. Если команда
push_back или push_front вызывается для дека, размер которого равен максимально
возможному, тоже нужно вывести 'error'.
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

    def pop_back(self):
        if self.isEmpty():
            return 'error'
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size_queue -= 1
        return x

    def pop_front(self):
        if self.isEmpty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size_queue -= 1
        return x

    def push_front(self, item):
        if self.size_queue < self.max_n:
            if self.queue[self.head] is None:
                self.queue[self.head] = item
            else:
                self.head = (self.head - 1) % self.max_n
                self.queue[self.head] = item
            self.size_queue += 1
            return ''

    def push_back(self, item):
        if self.size_queue < self.max_n:
            if self.queue[self.tail] is None:
                self.queue[self.tail] = item
            else:
                self.tail = (self.tail - 1) % self.max_n
                self.queue[self.tail] = item
            self.size_queue += 1
            return ''

    def size(self):
        return self.size_queue


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()

string, template = input_file[0], input_file[1]

output_file = ''

count_commands = int(input_file[0])
queue_size = int(input_file[1])
commands = input_file[2:]
queue = MyQueueSized(queue_size)
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'push_back':
        output_file += str(queue.push_back(int(command[1])))
    elif command[0] == 'push_front':
        output_file += str(queue.push_front(int(command[1])))
    elif command[0] == 'pop_front':
        output_file += str(queue.pop_front()) + '\n'
    elif command[0] == 'pop_back':
        output_file += str(queue.pop_back()) + '\n'

print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
