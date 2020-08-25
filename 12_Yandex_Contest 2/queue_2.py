#from queue import Queue


class Queue:
    def __init__(self,  n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def get(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


q = Queue(3)
q.put(1)
print(q.queue)
q.put(2)
print(q.queue)
print(q.get()) # 1
q.put(3)
print(q.queue) # [None, 2, 3]
q.put(4)
print(q.queue) # [4, 2, 3]
print(q.get()) # 2

