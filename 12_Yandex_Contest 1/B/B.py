from collections import defaultdict
f = open('input.txt')
ids = f.read()
f.close()
hash_table = defaultdict(int)
id = ids.split()[:-1]
k = int(ids.split()[-1:][0])
for i in id:
    hash_table[i] += 1
output = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
out_file = ''
for i in range(k):
    out_file = out_file + output[i][0] + ' '
f = open('output.txt', 'w')
f.write(str(out_file) + '\n')
f.close()
