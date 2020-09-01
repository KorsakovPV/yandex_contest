"""
C. Подпоследовательность

Вася любит играть в игру Подпоследовательность. Даны 2 строки, и нужно понять,
является ли первая из них подпоследовательностью второй. Когда строки
достаточно длинные, иногда очень трудно получить ответ на этот вопрос, просто
посмотрев на них. Помогите Васе, напишите функцию, которая решает эту задачу.

Формат ввода
В первой строке записана строка s.

Во второй — строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят
100000.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе — False.
"""


def subsequence(input_file):
    s = input_file.strip().split()
    if len(s)>1:
        sub_string = [x for x in s[0]]
        main_string = [x for x in s[1]]
    else:
        sub_string = []
        main_string = [x for x in s[0]]
    # sub_string.sort()
    # main_string.sort()

    while len(main_string) > 0 and len(sub_string) > 0:
        i_sub_string = main_string.pop()
        if i_sub_string == sub_string[len(sub_string) - 1]:
            sub_string.pop()

    if sub_string == []:
        return 'True' + '\n'
    else:
        return 'False' + '\n'


def main(input_file):
    f = open(input_file)
    input_file = f.read()
    f.close()

    return str(subsequence(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    f = open('output.txt', 'w')

    f.write(main(input_txt) + '\n')

    f.close()

    # print(main(input_txt))

    assert main('input1.txt') == 'True\n', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == 'False\n', 'input2.txt error\n' + main(
        'input2.txt')
    assert main('input3.txt') == 'True\n', 'input3.txt error\n' + main(
        'input3.txt')
    assert main('input4.txt') == 'True\n', 'input4.txt error\n' + main(
        'input4.txt')