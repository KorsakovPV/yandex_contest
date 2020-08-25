f = open('input.txt')
input_file = f.read()
f.close()
input_string = input_file.split()

len_list_score, list_score= int(input_string[0]), input_string[1:]

#try:
#    while True:
#        list_score.remove('0')
#except ValueError:
#    pass

for i in range(len_list_score):
    if list_score[len_list_score - i -1] == '0':
        del list_score[len_list_score - i - 1]

output_file = ''
for i in list_score:
    output_file += i + ' '

f = open('output.txt', 'w')
f.write(str(output_file) + '\n')
f.close()
