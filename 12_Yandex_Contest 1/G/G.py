f = open('input.txt')
input_file = f.read()
f.close()
input_data = input_file.split()

if ''.join(sorted(input_data[0]))==''.join(sorted(input_data[1])):
    output_data = 'True'
else:
    output_data = 'False'

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
