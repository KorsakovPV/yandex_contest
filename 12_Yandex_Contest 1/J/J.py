f = open('input.txt')
input_file = f.read().split()
f.close()
n, input_data = input_file[0], input_file[1:]
output_data = 0
for i in input_data:
    output_data ^= int(i)

f = open('output.txt', 'w')
f.write(str(output_data) + '\n')
f.close()
