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
"""

f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()

string, template = input_file[0], input_file[1]

output_file = ''



# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
