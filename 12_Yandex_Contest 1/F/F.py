from collections import defaultdict

f = open('input.txt')
input_file = f.read()
f.close()
input_data = input_file.split()
n, data = input_data[:1], input_data[1:]
hash_table = defaultdict(int)
for i in data:
    hash_table[i] += 1
    if hash_table[i] == 2:
        output_data = i
        break

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
