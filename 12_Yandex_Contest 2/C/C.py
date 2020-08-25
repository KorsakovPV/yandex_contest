"""
C. Подстроки

На вход подается строка. Нужно определить длину наибольшей подстроки, которая
не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из латинских букв. Длина строки не превосходит 10000.

Формат вывода
Одно число - ответ на задачу.
"""
def func(input_file):
    max_count = ''
    j = 0
    for i in range(len(input_file)):
        if input_file[i] in input_file[j:i]:
            if len(max_count) < len(input_file[j:i]):
                max_count = input_file[j:i]
                #j += 1
            while input_file[i] in input_file[j:i]:
                j += 1

    if len(max_count) < len(input_file[j:i+1]):
        max_count = input_file[j:i+1]

    output_file = str(len(max_count))
    #print(max_count, output_file)
    return output_file


f = open('input.txt')
input_file = f.read().rstrip()#.split()
f.close()

"""print('1=',func('1'))
print('1=',func('11'))
print('12=',func('12'))
print('12=',func('112'))
print('12=',func('122'))
print('12=',func('1223'))
print('12=',func('12223'))
print('12=',func('11223'))
"""

output_file = func(input_file)

f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()

