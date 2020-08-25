"""
O. Шифрование

Алла реализовывала алгоритм шифрования и что-то напутала. В итоге после
расшифровки буквы в словах получились в произвольном порядке. Помогите Алле
разобраться с проблемой. Напишите функцию, принимающую на вход строку и шаблон
и определяющую, сколько анаграмм шаблона будет в строке.

Напомним, что два слова — анаграммы, если одно из них можно получить из
другого, переставив буквы. Например, слова «кот» и «ток».

Формат ввода
В первой строке задана строка, в которой будет производиться поиск. Во
второй - шаблон. Длина обеих строк не превосходит 1000 и длина шаблона не может
быть больше длины строки для поиска.

Формат вывода
Одно число - ответ на задачу.
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

output_file = ''



# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
