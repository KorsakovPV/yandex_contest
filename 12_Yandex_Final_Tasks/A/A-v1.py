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


def calc(input_file):
    def addition(operand1, operand2):
        return operand2 + operand1

    def subtraction(operand1, operand2):
        return operand2 - operand1

    def multiplication(operand1, operand2):
        return operand2 * operand1

    def division(operand1, operand2):
        return operand2 // operand1

    d = {'+': addition,
         '-': subtraction,
         '*': multiplication,
         '/': division}

    for i in input_file:
        if i in d.keys():
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.push(d[i](operand1, operand2))
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    f = open('input.txt')
    input_file = f.read().rstrip().split()
    f.close()

    stack = Stack()

    output_file = str(calc(input_file))
    print(output_file)
    f = open('output.txt', 'w')
    f.write(output_file + '\n')
    f.close()
