"""
C. Подпоследовательность

Вася любит играть в игру Подпоследовательность. Даны 2 строки, и нужно понять,
является ли первая из них подпоследовательностью второй. Когда строки
достаточно длинные, иногда очень трудно получить ответ на этот вопрос, просто
посмотрев на них. Помогите Васе, напишите функцию, которая решает эту задачу.

Формат ввода
В первой строке записана строка s.

Во второй — строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят
100000.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе — False.
"""


s = input()
t = input()
it = iter(t)
print(all(c in it for c in s))