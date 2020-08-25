def func(input_file):

    def neighbor(ntt,mtt):
        if 0 <= ntt <=n-1 and 0<= mtt <= m-1:
            return int(data[ntt][mtt])
        return 0

    n, m, input_data, nt, mt = int(input_file[0]), int(input_file[1]), input_file[2:-2], int(input_file[-2]), int(input_file[-1])
    #if nt < 0 or nt >= n or mt < 0 or mt >= m:
    #    return ''
        
    data = [input_data[i:i+m] for i in range(0, len(input_data), m)]
    neighbors = list()
    neighbors.append(neighbor(nt-1,mt))
    neighbors.append(neighbor(nt+1,mt))
    neighbors.append(neighbor(nt,mt-1))
    neighbors.append(neighbor(nt,mt+1))
    neighbors.sort()
    output = ''

    for i in neighbors:
        if i != 0:
            output += str(i)+ ' '

    return output[:-1]

f = open('input.txt')
input_file = f.read().rstrip()
f.close()

output_file = func(input_file.split())
#print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
