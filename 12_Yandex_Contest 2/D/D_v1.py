def func(input_file):
    
    n, m, input_data, nt, mt = int(input_file[0]), int(input_file[1]), input_file[2:-2], int(input_file[-2]), int(input_file[-1])
 
    data = [input_data[i:i+m] for i in range(0, len(input_data), m)]

    neighbors = list()

    if 0 <= nt+1 <=n-1 and 0<= mt <= m-1:
        neighbors.append((data[nt+1][mt]))
    if 0 <= nt-1 <=n-1 and 0<= mt <= m-1:
        neighbors.append((data[nt-1][mt]))
    if 0 <= nt <=n-1 and 0<= mt+1 <= m-1:
        neighbors.append((data[nt][mt+1]))
    if 0 <= nt <=n-1 and 0<= mt-1 <= m-1:
        neighbors.append((data[nt][mt-1]))

    neighbors.sort(key=int)

    return ' '.join(neighbors)

f = open('input.txt')
input_file = f.read().rstrip()
f.close()

output_file = func(input_file.split())
#print(output_file)
f = open('output.txt', 'w')
f.write(output_file + '\n')
f.close()
