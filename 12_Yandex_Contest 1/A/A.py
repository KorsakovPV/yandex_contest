"""
A. Значения функции

Младший брат Аллы Вася делает тест по математике: вычисляет значение функций в
различных точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мама
разрешила мальчику пойти на улицу только после того, как он закончит тест. К
сожалению, Вася пока не умеет программировать. Зато Алла умеет. Она решила
помочь брату и написала код функции y = ax2 + bx + c. И вы напишите.

Формат ввода
На вход через пробел подаются числа a, x, b, c.
"""

f = open('input.txt')
l = f.read()
f.close()
a, x, b, c = [int(i) for i in l.split(' ')]
y = a*x*x+b*x+c
f = open('output.txt', 'w')
f.write(str(y) + '\n')
f.close()

