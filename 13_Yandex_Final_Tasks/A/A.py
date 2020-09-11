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


def solution(a, b, nod):
    return 0



def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    n = int(input_file[0])
    size_data_center = list(map(int, input_file[1].rstrip().split()))
    return solution(n, size_data_center)


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))

    assert main('input1.txt') == 11, 'input1.txt error\n' + str(
        main('input1.txt'))
    assert main('input2.txt') == 16, 'input2.txt error\n' + str(
        main('input2.txt'))
    assert main('input3.txt') == 12, 'input3.txt error\n' + str(
        main('input3.txt'))
