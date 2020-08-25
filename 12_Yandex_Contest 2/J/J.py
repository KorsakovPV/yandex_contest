class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty():
            self.max.append(item)
        elif self.max[len(self.max)-1]<item:
            self.max.append(item)     
        self.items.append(item)

    def pop(self):
        if len(self.items)>0 and len(self.max)>0:
            if self.items[len(self.items)-1]==self.max[len(self.max)-1]:
                self.max.pop()
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return 'None\n'
        else:
            return str(self.max[len(self.max)-1])+'\n'


f = open('input3.txt')
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
