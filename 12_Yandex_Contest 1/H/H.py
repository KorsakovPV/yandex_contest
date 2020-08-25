import re

f = open('input.txt')
input_file = f.read()
f.close()
input_data = re.sub('[^a-z0-9]', '', input_file.lower().strip())
output_data = str(input_data[::-1] == input_data)
print(output_data)
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
