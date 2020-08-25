f = open('input.txt')
l = f.read()
f.close()
a, x, b, c = [int(i) for i in l.split(' ')]
y = a*x*x+b*x+c
f = open('output.txt', 'w')
f.write(str(y) + '\n')
f.close()

