def dec_to_bin(num):
    values = '01'
    d, e = divmod(num,2)
    if d>=1:
        return dec_to_bin(d) + values[e]
    else:
        return values[e]

f = open('input.txt')
input_file = f.read()

output = str(dec_to_bin(int(input_file)))
output_counter = output.count('1')

f = open('output.txt', 'w')
f.write((str(output_counter)) + '\n')
f.close()