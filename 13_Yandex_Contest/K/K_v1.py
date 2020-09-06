"""
K. Ипотека

Дочь Кондратия Евлампия решила купить в ипотеку несколько домов на территории
Трешландии.

Она нашла n объявлений о продаже. Известна стоимость каждого дома в
трешландских франках. Евлампия может позволить себе взять ипотеку на общую
сумму k франков. Нужно помочь ей определить, какое наибольшее количество домов
можно купить на эти деньги.

Формат ввода
В первой строке через пробел записаны целые числа n и k

n - количество домов, которые рассматривает Евлампия, оно не превосходит 1000

k - общий бюджет, не превосходит 10000

В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не
превосходит 10000. Все стоимости - целые числа.

Формат вывода
Выведите число, равное максимально возможному числу домов, которые может купить
Евлампия


"""

nk = [int(i) for i in input().split()]
houses_costs = [int(i) for i in input().split()]
print(10)
houses_costs.sort()
i = 0
n = len(houses_costs)
while houses_costs[i] <= nk[1]:
    nk[1] -= houses_costs[i]
    i += 1
    if i == n:
        break
print(i)
