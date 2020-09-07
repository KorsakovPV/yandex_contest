"""
A. Рекурсивные числа Фибоначчи

Помогите жителям Трешландии понять, сколько питомцев они могут завести.
Напишите рекурсивную реализацию функции, определяющей по номеру значение n-ого
числа Фибоначчи.
Формат ввода
На вход подается n - целое число в диапазоне от 0 до 30.
Формат вывода
Нужно вывести n-ое число Фибоначчи.

Примечания
Функция должна быть реализована рекурсивно.
Обратите внимание на то, что в этом спринте считывать данные нужно из файла
input.txt.
"""

def fibonacci_numbers(n):
    assert n >= 0
    # if n==0:
    #     return 1
    # elif n==1:
    #     return 1
    # return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)
    return 1 if n <=1 else fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)

def main(input_file):
    with open(input_file) as f:
        input_file = int(f.read().rstrip().split()[0])

    return str(fibonacci_numbers(input_file))


if __name__ == '__main__':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(main(input_txt) + '\n')

    assert main('input1.txt') == '3', 'input1.txt error\n' + main(
        'input1.txt')
    assert main('input2.txt') == '1', 'input2.txt error\n' + main(
        'input2.txt')
