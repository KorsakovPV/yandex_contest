from itertools import permutations, combinations

f = open('input.txt')
input_file = f.read().split()
#n = int(input_file[0])
score_data = list(map(int, input_file[1:]))
#score_data = input_file[1:]
#print(score_data)
score_data.sort()#key=None, reverse=True
#score_data.reverse()
#print(score_data)
max_product = -1

for i1 in range(len(score_data)-2):
    left = i1 + 1
    right = len(score_data) - 1
    while left < right:
        sum = score_data[i1] + score_data [left] + score_data[right]
        if sum == 0 and score_data[i1] * score_data [left] * score_data[right] > max_product:
            max_product = score_data[i1] * score_data [left] * score_data[right]
        if sum > 0:
            right -= 1
        else:
            left += 1


"""n=0
for i in range(n-2): 
    score_amount = int(score_data[i])+int(score_data[i+1])+int(score_data[i+2])
    score_multiplication = int(score_data[i])*int(score_data[i+1])*int(score_data[i+2])
    if score_amount == 0 and score_multiplication > 0:
        max_product = score_multiplication"""


output_data = str(max_product)
#print(output_data)
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
"""
for i1 in range(n):
    for i2 in range(i1+1, n):
        for i3 in range(i2+1, n):
            score_amount = int(score_data[i1])+int(score_data[i2])+int(score_data[i3])
            score_multiplication = int(score_data[i1])*int(score_data[i2])*int(score_data[i3])
            if score_amount == 0 and max_product < score_multiplication:
                max_product = score_multiplication
"""
"""
for item in combinations(score_data, 3):
    score_amount = int(item[0])+int(item[1])+int(item[2])
    score_multiplication = int(item[0])*int(item[1])*int(item[2])
    if score_amount == 0 and max_product < score_multiplication:
        max_product = score_multiplication
    print(item, score_amount, score_multiplication)
"""


