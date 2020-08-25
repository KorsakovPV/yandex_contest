import re

f = open('input.txt')
input_file = f.read().rstrip().split('\n')
f.close()
input_string = ''
for i in input_file[0]:
    if i in '({[]})':
        input_string += i


#input_data = re.sub('[^a-z0-9]', '', input_file.lower().strip())

output_file = str(input_string == input_string[::1])
        
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
