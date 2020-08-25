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

def findAnagrams(string, template):
    len_string = len(string)
    len_template = len(template)
    hash_string = 0
    hash_template = 0
    count = 0
    if len_template > len_string:
        return []
    for i in range(len_template):
        hash_string = hash_string + hash(string[i])
        hash_template = hash_template + hash(template[i])
    if hash_string == hash_template:
        count += 1
    for i in range(len_template, len_string):
        hash_string += hash(string[i]) - hash(string[i - len_template])
        if hash_string == hash_template:
            count += 1
    return count


f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()

string, template = input_file[0], input_file[1]

output_file = ''

output_file = str(findAnagrams(string, template))

# print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
