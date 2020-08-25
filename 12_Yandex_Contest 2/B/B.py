f = open('input2.txt')
input_file = f.read().rstrip().split()
f.close()
#print(input_file)
n, m, input_data = int(input_file[0]), int(input_file[1]), input_file[2:]
#print(unique_courses)
output_file = ''#'\n'.join((unique_courses))#sorted
for i in range(m):
    for j in range(n):
        #print(input_data[i+j*m], end = ' ')
        output_file += input_data[i+j*m]+' '
    #print('')
    output_file += '\n'
print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()

