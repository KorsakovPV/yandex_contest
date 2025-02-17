"""
P. Комбинации

На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько
букв. Примерно так:

2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'

Вам известно в каком порядке были нажаты клавиши телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно.

Формат вывода
Выведите все возможные комбинации букв через пробел.
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
                
    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])
                    
    output = []
    if digits:
        backtrack("", digits)
    return output

f = open('input.txt')
input_file = f.read().strip()
digits = (input_file)
output_data = ' '.join(letterCombinations(digits))

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()

