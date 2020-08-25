#word = list(input())
word = 'treeжжвороварыовывраывлорыворалвыраварлывоарлоацуюиоуиавржрсжд рстывтабвавабвтбт'
def sort_letters(a):
    b = []
    for i in range(1, 10001):
        c = []
        for letter in a:
            if a.count(letter) == i:
                c.append(letter)
        c = sorted(c, reverse=True)
        b+=c
        if len(b) == len(a):
            break
    b.reverse()
    print(''.join(b))
sort_letters(word)

from collections import Counter, defaultdict
letter_counts = Counter(word)
