"""
A. Фотокопии

Евлампия очень любит постить фотографии в инстаграм. Но она боится, что данные
с сервера могут пропасть. Поэтому она приняла решения хранить все изображения
также в Трешландских датацентрах в двух экземплярах.

Всего есть N датацентров, в каждом из которых можно разместить fi фотографий,
где i = 0..N-1.

Но хранить две копии фотографии в одном датацентре ненадежно. Вдруг с ним
что-нибудь случится. Поэтому так делать нельзя. Нужно определить, какое
максимальное число фотографий Евлампия сможет сохранить.

Формат ввода
В первой строке записано n - количество датацентров. Оно не превосходит 10000.

В следующей строке через пробел записаны n чисел - вместимости датацентров в
штуках фотографий. Каждое из чисел не превосходит 10000.

Формат вывода
Нужно вывести число, равное максимальному количеству фотографий, для которых
можно хранить копии в этих датацентрах.

Пример 1
Ввод
4
8 7 4 3
Вывод
11
Пример 2
Ввод
5
8 7 7 6 5
Вывод
16
Пример 3
Ввод
4
1 6 9 8
Вывод
12
Примечания
Для решения нужно использовать жадный алгоритм.

Для примера приведено несколько жадных стратегий. Нет гарантии, что каждая из
них являются верной для любых входных данных. Можно выбрать и реализовать одну
из них, удостоверившись, что она является корректной, или предложить свой
вариант.

Стратегия 1:

Выбрать два датацентра с наименьшей вместимостью и помещать в них столько
фотографий, сколько возможно.

Стратегия 2:

Выбрать датацентр с наибольшей вместимостью и датацентр с наименьшей
вместимостью и помещать в них столько фотографий, сколько возможно.

Стратегия 3:

Выбрать два датацентра с наибольшей вместимостью и помещать в них наибольшее
возможное количество фотографий.

Стратегия 4:

Выбрать один датацентр с наибольшей вместимостью и один датацентр с наименьшей
вместимостью помещать в них по одной фотографии.
"""


# 34439123
# O(n)
def solution(n, size_data_center):
    max_size = max(size_data_center)
    amount = sum(size_data_center)
    half_amount = amount // 2
    if half_amount < max_size:
        return amount - max_size
    else:
        return half_amount

# 34442276
# O(n*n log n) O(n^2)
def solution2(n, size_data_center):
    count = 0
    size_data_center.sort(reverse=True)
    while len(size_data_center) > 1:
        size_data_center[0] -= 1
        size_data_center[len(size_data_center) - 1] -= 1
        size_data_center.sort(reverse=True)
        while size_data_center[len(size_data_center) - 1] == 0:
            size_data_center.pop()
        # if size_data_center[len(size_data_center) - 1] == 0:
        #     size_data_center.pop()
        # if size_data_center[len(size_data_center) - 1] == 0:
        #     size_data_center.pop()
        count += 1
    return int(count)

#
def solution3(n, size_data_center):
    max_size = sum(size_data_center)
    size_data_center.sort(reverse=True)
    count = 0
    while len(size_data_center) > 1 or max_size < count:
        if len(size_data_center) <= 4:
            size_data_center.sort(reverse=True)
        size_data_center[0] -= 1
        size_data_center[len(size_data_center) - 1] -= 1
        if size_data_center[len(size_data_center) - 1] == 0:
            size_data_center.pop()
            size_data_center.sort(reverse=True)
        count += 1

    return int(count)

def solution4(n, arr):
    count = 0
    left = 0
    right = n
    while left < right:
        arr[left] -= 1
        arr[right] -= 1
        count += 1
        while arr[right] < arr[right - 1]:
            arr[right], arr[right - 1] = arr[right - 1], arr[right]
            right -= 1
        right = n
        while arr[left] == 0 and left < right:
            left += 1
    return count


def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    size_data_center = list(map(int, input_file[1].rstrip().split()))
    sol = solution4(n, size_data_center)
    return sol


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = str(main(input_file))
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(input_file) == 11, 'input1.txt error\n' + str(main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(input_file) == 16, 'input2.txt error\n' + str(main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == 12, 'input3.txt error\n' + str(main(input_file))
