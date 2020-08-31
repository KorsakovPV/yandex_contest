"""
B. Биржа

Рита захотела подзаработать денег и решила поиграть на бирже. Она подумала, что
сначала нужно потренироваться на исторических данных.

Дан массив цен акций. На i-й позиции массива — цена в i-й день. Акции можно
покупать и продавать, но только по одной штуке. В одно время не должно быть
более одной открытой транзакции.

Помогите Рите выяснить, какую максимальную прибыль она может получить.

Формат ввода
В первой строке записано целое число n. Оно находится в диапазоне от 0 до
10000.

Во второй строке через пробел записаны n целых чисел в диапазоне от 0 до 1000.

Формат вывода
Нужно вывести число, равное максимально возможной прибыли за эти дни.
"""


class Stack:
    def __init__(self, n):
        self.stock_price = []
        self.profit = 0
        self.extremum = []


    def push(self, id, price):
        self.stock_price.append(price)

    def max_profit(self):

        for i in range(len(self.stock_price) - 1):
            if self.stock_price[i] < self.stock_price[i+1]:
                self.profit += self.stock_price[i+1] - self.stock_price[i]
        return self.profit


def calc(input_file):
    input_file = input_file.strip().split()
    n = input_file[0]
    stock_prices = input_file[1:]
    output_file = ''

    stack = Stack(int(n))

    for i in range(len(stock_prices)):
        stack.push(i, int(stock_prices[i]))

    output_file += (str(stack.max_profit()) + '\n')

    return output_file


def main(input_file):
    f = open(input_file)
    input_file = f.read()
    f.close()

    return str(calc(input_file))


if __name__ == '__main__':
    input_txt = 'input1.txt'

    f = open('output.txt', 'w')

    f.write(main(input_txt) + '\n')

    f.close()

    # print(main(input_txt))

    assert main(
        'input1.txt') == '7\n', "input1.txt error\n" + main(
        'input1.txt')
    assert main(
        'input2.txt') == '4\n', "input2.txt error\n" + main(
        'input2.txt')
    assert main(
        'input3.txt') == '22\n', "input3.txt error\n" + main(
        'input3.txt')
    assert main(
        'input4.txt') == '0\n', "input4.txt error\n" + main(
        'input4.txt')