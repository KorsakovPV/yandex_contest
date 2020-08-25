def func(input_file):
    #print(input_file)

    #output_file = ''#'\n'.join((unique_courses))#sorted
    max_count = ''
    #count = ''
    j = 0
    for i in range(len(input_file)):
        for j in range(i, len(input_file)):
            print(input_file[i:j+1])
            if input_file[j] in input_file[i:j+1]:
            




    #output_file = str(len(max_count))
    #print(max_count, output_file)
    return max_count


f = open('input.txt')
input_file = f.read().rstrip()#.split()
f.close()

"""print('1=',func('1'))
print('1=',func('11'))
print('12=',func('12'))
print('12=',func('112'))
print('12=',func('122'))
print('12 23=',func('1223'))"""


output_file = func(input_file)

f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()

