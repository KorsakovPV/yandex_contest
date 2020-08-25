"""
P. Списочная очередь

Любимый вариант очереди Тимофея - очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
методы get, put, size.

Формат ввода
В первой строке записано количество команд n - целое число, не превосходящее
1000. В каждой из следующих n строк записана команда: get, put, или size.

Формат вывода
При вызове метода get напечатайте возвращаемое значение. Если метод get
вызывается у пустой очереди, нужно напечатать 'error'. При вызове метода
size - вывести размер очереди.

Примечания
Все операции должны выполняться за O(1).
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

    def get(self):
        if self.isEmpty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size_queue -= 1
        return x

    def put(self, item):
        if self.size_queue < self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
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
commands = input_file[1:]
queue = MyQueueSized(count_commands)
output_file = ''

for i in commands:
    command = i.split()
    if command[0] == 'put':
        output_file += str(queue.put(int(command[1])))
    elif command[0] == 'get':
        output_file += str(queue.get()) + '\n'
    elif command[0] == 'size':
        output_file += str(queue.size()) + '\n'

# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
