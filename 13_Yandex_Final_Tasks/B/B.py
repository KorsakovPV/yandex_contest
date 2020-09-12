"""
B. Поиск в сломанном массиве

Алла ошиблась со структурой данных. Она решила хранить массив в кольцевом
буфере.
Проблема в том, что массив был отсортирован. И в нем можно было искать элемент
за логарифмическое время. Алла скопировала данные из кольцевого буфера а
обычный массив. Но он больше не является отсортированным. Тем не менее нужно
обеспечить возможность находить в нем элемент за O(logn).

Формат ввода
В первой строке записано число n - длина массива.
Во второй строке записано положительное число k - искомый элемент.
n и k не превосходят 1000.
Далее в строку через пробел записаны n положительных чисел, каждое из которых
не превосходит 1000.

Формат вывода
Выведите индекс искомого элемента в массиве, если он найден. Иначе выведите -1.

Пример 1
Ввод
8
3
1 2 3 5 6 7 9 0
Вывод
2
Пример 2
Ввод
7
5
0 2 6 7 8 9 10
Вывод
-1
Пример 3
Ввод
1
1
1
Вывод
0
Примечания
Можно предполагать, что в массиве только уникальные элементы.
Сортировать массив нельзя.
Объем дополнительной памяти, помимо массива, в который считываются данные, и
стека вызовов функций, O(1).
"""


#34378396
def solution(data, target):
    l, r = 0, len(data) - 1
    while l <= r:
        m = (r + l) // 2
        if data[m] == target:
            return m
        elif data[m] <= data[r]:
            if target > data[m] and target <= data[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target >= data[l] and target < data[m]:
                r = m - 1
            else:
                l = m + 1
    return -1


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    n = int(input_file[0])
    k = int(input_file[1])
    data = list(map(int, input_file[2].rstrip().split()))
    sol = solution(data, k)
    return sol


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))

    assert main('input1.txt') == 2, 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == -1, 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == 0, 'input3.txt error\n' + str(
        main('input3.txt'))
