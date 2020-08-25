"""
H. Палиндром

А теперь помогите Васе понять, будет ли фраза палиндромом. Учитываются
только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только
латинские.

Формат вывода
Выведите True, если фраза является палиндромом и False, если не является.
"""

import re

f = open('input.txt')
input_file = f.read()
f.close()
input_data = re.sub('[^a-z0-9]', '', input_file.lower().strip())
output_data = str(input_data[::-1] == input_data)
print(output_data)
f = open('output.txt', 'w')
f.write(output_data + '\n')
f.close()
