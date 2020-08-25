from queue import Queue

queue = Queue()
queue.put('a')
queue.put('b')
size_of_queue = queue.qsize()
print(size_of_queue)
elem = queue.get()
size_of_queue = queue.qsize()
print(size_of_queue)
print(elem)