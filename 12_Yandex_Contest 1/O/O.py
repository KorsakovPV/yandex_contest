f = open('input.txt')
input_file = f.read().strip().split('\n')

m = int(input_file[1])
k = int(input_file[2])
string_first = input_file[0].split()
strint_second = input_file[3].split()

for i in range(len(string_first)):
    if int(string_first[i]) >= int(strint_second[0]) or string_first[i]=='0':
        string_first.insert(i,strint_second[0])
        strint_second.remove(strint_second[0])
        if len(strint_second)==0:
            break


output_data = ' '.join(string_first[:-k])

f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
