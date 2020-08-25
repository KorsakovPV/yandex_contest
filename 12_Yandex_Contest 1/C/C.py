f = open('input.txt')
input_file = f.read()
f.close()
input_string = input_file.split()
len_list_form, list_form, k = int(input_string[0]), input_string[1:-1], int(input_string[-1])
output = 0
for i in range(len_list_form):
    output += 10 ** (len_list_form - i - 1) * int(list_form[i])
output += k
output = str(output)
output_file = ''
for i in output:
    output_file += i + ' '

f = open('output.txt', 'w')
f.write(str(output_file) + '\n')
f.close()
