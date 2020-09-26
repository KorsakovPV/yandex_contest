"""
I. Дерево поиска

Прабабке Кондратия уже 182 года. Домна Тарасовна часто любит выходить в сад
погулять. Сегодня, выходя на прогулку, она забыла очки, без которых почти
ничего не видит. Но она может прекрасно ориентироваться при помощи трости,
которой она определила, что приближается к дереву. Что бы увидела баба Домна,
если бы не забыла очки?
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value

INT_MAX = 4294967296

INT_MIN = -4294967296

def solution(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

def isBSTUtil(node, mini, maxi):

    if node is None:
        return True

    if node.value < mini or node.value > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.value - 1) and
            isBSTUtil(node.right, node.value + 1, maxi))

# def solution1(node):
#     if node.left is None and \
#             node.right is None:
#         return True
#     elif node.left is not None and \
#             node.right is None:
#         return solution1(node.left) and \
#                node.left.value < node.value
#     elif node.left is None and \
#             node.right is not None:
#         return solution1(node.right) and \
#                node.value < node.right.value
#     else:
#         return solution1(node.right) and \
#                node.left.value < node.value and \
#                node.value < node.right.value


def main():
    return 0


if __name__ == '__main__':
    node12 = Node(20)
    node11 = Node(18)
    node10 = Node(6)
    node09 = Node(3)
    node08 = Node(1)
    node07 = Node(19, node11, node12)
    node06 = Node(16)
    node05 = Node(5, node10)
    node04 = Node(2, node08, node09)
    node03 = Node(17, node06, node07)
    node02 = Node(4, node04, node05)
    node01 = Node(7, node02, node03)

    print(solution(node01))

    # test()
