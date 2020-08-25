from math import log
f = open('input.txt')
input_file = int(f.read().strip())
output_data = str(log(input_file,4).is_integer())
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
