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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return 'None\n'
        else:
            max_value = int(self.items[0])
            for i in self.items:
                if int(i)>int(max_value):
                    max_value = int(i)
            return str(max_value)+'\n'
        return '0'


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
        
#print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
