def letterCombinations(digits):
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
                
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
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

