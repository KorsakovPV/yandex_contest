"""
A. Кружки

Напишите код для решения задачи про поиск кружков, которые посещает хотя бы
один ученик. Ваше решение должно задействовать O(1) дополнительной памяти (то
есть помимо памяти, выделенной под массив visited_optional_courses)

Формат ввода
В первой строке записано количество кружков n, целое число, не превосходящее
10000 В следующих n строках записаны названия кружков.

Формат вывода
Выведите уникальные названия кружков по одному на строке, в порядке появления
во входных данных.
"""

f = open('input.txt')
input_file = f.read().split('\n')
f.close()
# print(input_file)
n, visited_optional_courses = input_file[0], input_file[1:]
unique_courses = list()
for course in visited_optional_courses:
    if course != '' and course not in unique_courses:
        unique_courses.append(course)
# print(unique_courses)
output_file = '\n'.join((unique_courses))  # sorted
print(output_file)
# sorted(unique_courses)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()

# Решение Владимира
m = n

visited_optional_courses = [i for n, i in enumerate(visited_optional_courses)
                            if
                            i not in visited_optional_courses[:n] and i != '']
print('Владимир')
print('\n'.join(visited_optional_courses))
