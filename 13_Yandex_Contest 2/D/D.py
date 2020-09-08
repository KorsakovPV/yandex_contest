"""
D. Последняя цифра

У одного жителя деревни Упыревка очень старый компьютер. На экран он может
выводить только одну цифру, причем последнюю из тех, что выводится в
стандартный поток вывода. Помогите жителю Упыревки понять, что должно быть
выведено на экран, когда он запустит программу для вычисления n - ого числа
Фибоначчи.

Формат ввода
На вход подается n - целое число в диапазоне от 0 до 10000

Формат вывода
Нужно вывести одну цифру, последнюю в числе, равному n - ому числу Фибоначчи

Примечания
В решении не должно вычисляться само число Фибоначчи. Диапазон подаваемых на
вход данных достаточно большой.
"""

def fibonacci_numbers(n):
    assert n >= 0
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return str(f1)[-1]

def main(input_file):
    with open(input_file) as f:
        input_file = int(f.read().rstrip().split()[0])

    return str(fibonacci_numbers(input_file))


if __name__ == '__main__':
    cache = {}
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == '3', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1', 'input2.txt error\n' + main(
        'input2.txt')