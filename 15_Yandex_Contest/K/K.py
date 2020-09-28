"""
C. Генеалогическое древо

Гуляя по вилле Кондратия, ребята нашли генеалогическое древо его семьи. Им
стало интересно, сколько лет прожили члены семьи разных поколений.

Помогите ребятам это выяснить.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def solution(node, numeral=0, amount=0):
    numeral = numeral * 10 + node.value
    if node.left is None and node.right is None:
        return amount + numeral
    elif node.left is None:
        return solution(node.right, numeral, amount)
    elif node.right is None:
        return solution(node.left, numeral, amount)
    else:
        return solution(node.left, numeral, amount)+solution(node.right, numeral, amount)


# def test():
#     assert solution(node01) == False, 'node01 error ' + str(solution(node01))
#     assert solution(node02) == False, 'node02 error ' + str(solution(node02))
#     assert solution(node03) == True, 'node03 error ' + str(solution(node03))
#     assert solution(node04) == True, 'node04 error ' + str(solution(node04))
#     assert solution(node05) == False, 'node05 error ' + str(solution(node05))
#     assert solution(node06) == True, 'node06 error ' + str(solution(node06))
#     assert solution(node07) == True, 'node07 error ' + str(solution(node07))
#     assert solution(node08) == True, 'node08 error ' + str(solution(node08))
#     assert solution(node09) == True, 'node09 error ' + str(solution(node09))
#     assert solution(node10) == True, 'node10 error ' + str(solution(node10))
#     assert solution(node11) == True, 'node11 error ' + str(solution(node11))
#     assert solution(node12) == True, 'node12 error ' + str(solution(node12))


def main():
    return 0


if __name__ == '__main__':
    node13 = Node(9)
    node12 = Node(1, node13)
    node11 = Node(0)
    node10 = Node(3)
    node09 = Node(5)
    node08 = Node(4)
    node07 = Node(6, node11, node12)
    node06 = Node(2)
    node05 = Node(9, node10)
    node04 = Node(8, node08, node09)
    node03 = Node(5, node06, node07)
    node02 = Node(3, node04, node05)
    node01 = Node(1, node02, node03)

    print(solution(node01))


