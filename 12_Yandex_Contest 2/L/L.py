"""
L. Скобочная последовательность

Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов. Если
вы с ней еще не сталкивались, то наверняка столкнётесь — она довольно
популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

- пустая строка — правильная скобочная последовательность;

- правильная скобочная последовательность, взятая в скобки одного типа, —
правильная скобочная последовательность;

- правильная скобочная последовательность с приписанной слева или справа
правильной скобочной последовательностью — тоже правильная.

На вход подается последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная,
иначе False.

Формат ввода
На вход подается одна строка, содержащая скобочную последовательность.

Формат вывода
True или False.
"""

def is_balanced(text, brackets="()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()
            else:
                return False
    return (not stack)
print(is_balanced(input()))


# f = open('input.txt')
# input_file = f.read().rstrip().split('\n')
# f.close()
# input_string = ''
# for i in input_file[0]:
#     if i in '({[]})':
#         input_string += i
#
# # input_data = re.sub('[^a-z0-9]', '', input_file.lower().strip())
#
# output_file = str(input_string == input_string[::1])
#
# f = open('output.txt', 'w')
# f.write(output_file + '\n')
# f.close()
