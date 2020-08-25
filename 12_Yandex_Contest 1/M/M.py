"""
M. Частоты

А теперь помогите Васе решить задачу по информатике. Он снова томится дома в
хорошую погоду.

На вход подается строка длиной от 1 до 10000 символов. Нужно отсортировать её в
порядке частот букв по встречаемости. Заглавные и строчные буквы считаются
разными. Если частота одинаковая, нужно применить вторичную сортировку
лексикографически.

Формат ввода
Одна строка длиной не более 10000 символов.

Формат вывода
Строка, в которой символы отсортированы в порядке убывания частотности.
"""


from collections import Counter, defaultdict

f = open('input.txt')
input_file = list(f.read().rstrip())
letter_counts = Counter(input_file)

r_letter_counts = defaultdict(list)
for letter, count in letter_counts.items():
    r_letter_counts[count].append(letter)

r_letter_counts_sorted = sorted(r_letter_counts.items(), key=lambda x: x[0],
                                reverse=True)

output_file = ''
for i in r_letter_counts_sorted:
    letter_sort = i[1]
    if len(i[1]) > 1:
        letter_sort.sort()
    for j in letter_sort:
        output_file += (i[0] * str(*j))

f = open('output.txt', 'w')
f.write(str(output_file) + '\n')
f.close()
