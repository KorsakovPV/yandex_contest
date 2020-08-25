"""
O. И снова Вася

Тимофей собирает метрики посещаемости сайта за последний месяц с двух серверов.
На каждой машине имеется список id пользователей, отсортированный в порядке от
минимального количества посещений к максимальному, вам известно число посещений
каждого пользователя. Пользователи, не посещавшие сайт в последний месяц, не
учитываются. Вам нужно сделать общий список числа посещений для двух серверов
так, чтобы в нем тоже числа шли по возрастанию. Так как сайт Тимофея очень
популярен, то данных о пользователях много, поэтому Тимофей может позволить
себе только линейное время работы алгоритма.

Формат ввода
В первой строке записаны количества посещений пользователей с первого сервера
через пробел, в конце - k нулей. Во второй строке записано число m - количество
пользователей, пришедших с первого сервера (без учета нулей в конце списка). В
третьей - число k - которое, помимо количества нулей, также является длиной
списка пользователей со второго сервера. В последней строке - список посещений
со второго сервера (k штук).

Количество посещений каждого пользователя не превосходит 10000, числа m и k
также не превосходят 10000

Формат вывода
В одной строке через пробел выведите элементы получившегося списка в
отсортированном порядке.
"""

f = open('input.txt')
input_file = f.read().strip().split('\n')

m = int(input_file[1])
k = int(input_file[2])
string_first = input_file[0].split()
strint_second = input_file[3].split()

for i in range(len(string_first)):
    if int(string_first[i]) >= int(strint_second[0]) or string_first[i] == '0':
        string_first.insert(i, strint_second[0])
        strint_second.remove(strint_second[0])
        if len(strint_second) == 0:
            break

output_data = ' '.join(string_first[:-k])

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
