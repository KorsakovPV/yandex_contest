f = open('input3.txt')
input_file = f.read().rstrip().split('\n')
f.close()
backpack = []
sum_weight = 0
c, n, arr = input_file[0], input_file[1], input_file[2:-1]
c = int(c)
arr = [x.split() for x in arr]
arr = enumerate(arr)
arr = sorted(arr, key=lambda x: (-int(x[1][0]), int(x[1][1])))
for i in arr:
    if sum_weight + int(i[1][1]) <= c:
        backpack.append(int(i[0]))
        sum_weight += int(i[1][1])
backpack.sort()
backpack = [str(i) for i in backpack]
output_file = ' '.join(backpack)
print(output_file)
f = open('output.txt', 'w')
f.write(output_file)
f.close()