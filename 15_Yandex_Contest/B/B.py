"""
B. Сбалансированное дерево

Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть про
сбалансированные деревья. Он решил написать функцию, которая определяет,
сбалансировано ли дерево.

Дерево считается сбалансированным, если левое и правое поддеревья каждого узла
отличаются по высоте не больше, чем на один.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def solution(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (abs(lh - rh) <= 1) and solution(root.left) is True and solution(
            root.right) is True:
        return True
    return False


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

    print(height(node01))
    print(solution(node01))
