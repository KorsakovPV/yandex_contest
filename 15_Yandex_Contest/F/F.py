"""
F. Вид слева

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


def solution(node, answer=[], index=0):
    if len(answer) - 1 < index:
        answer.append([])
    if answer[index]==[]:
        answer[index] = node.value
    index += 1
    if node.left is not None:
        solution(node.left, answer, index)
    if node.right is not None:
        solution(node.right, answer, index)
    return answer


def main():
    return 0


if __name__ == '__main__':
    node12 = Node(1)
    node11 = Node(0)
    node10 = Node(3)
    node09 = Node(15)
    node08 = Node(14)
    node07 = Node(6, node11, node12)
    node06 = Node(-2)
    node05 = Node(10, node10)
    node04 = Node(8, node08, node09)
    node03 = Node(5, node06, node07)
    node02 = Node(3, node04, node05)
    node01 = Node(1, node02, node03)

    print(solution(node01))

    # test()
