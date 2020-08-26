# 33850548
class Stack:
    def __init__(self):
        self.operands = []

    def is_empty(self):
        return self.operands == []

    def push(self, operand):
        self.operands.append(operand)

    def pop(self):
        if not self.is_empty():
            return self.operands.pop()


f = open('input2.txt')
input_file = f.read().rstrip().split()
f.close()

output_file = ''

stack = Stack()

for i in input_file:
    if i == '+':
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.push(operand1 + operand2)
    elif i == '-':
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.push(operand1 - operand2)
    elif i == '*':
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.push(operand1 * operand2)
    elif i == '/':
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.push(operand1 // operand2)
    else:
        stack.push(int(i))
output_file = str(stack.pop())
print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
