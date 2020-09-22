"""
A. Бриллианты

У Евлампии есть брошь с бриллиантами в виде дерева. В каждом узле дерева есть
какое-то количество бриллиантов. Помогите выяснить, какое максимальное
количество бриллиантов есть в одном узле.

В Трешландии может быть и отрицательное число драгоценных камней в украшении.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def solution(node):
    if node.left is None and node.right is None:
        return node.value
    if node.left is None and node.right is not None:
        return max(node.value, solution(node.right))
    if node.left is not None and node.right is None:
        return max(node.value, solution(node.left))
    return max(node.value, solution(node.left), solution(node.right))


def main(input_file):
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

print(solution(node05))
