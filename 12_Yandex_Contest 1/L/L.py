f = open('input.txt')
input_file = f.read().split()
s, t = list(input_file[0]), list(input_file[1])

for i in s:
    t.remove(i)

f = open('output.txt', 'w')
f.write(t[0] + '\n')
f.close()