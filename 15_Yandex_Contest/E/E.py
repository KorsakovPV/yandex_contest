"""
E. Деревья - близнецы

Евлампии на день рождения подарили два дерева. Кондратий сказал, что они
совершенно одинаковые. Но, по мнению Евлампии, они отличаются.

Помогите разрешить семейный спор!
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def solution(node1, node2):
    def func1(node, answer=[], index=0):
        if len(answer) - 1 < index:
            answer.append([])
        answer[index] += [node.value]
        index += 1
        if node.left is not None:
            func1(node.left, answer, index)
        if node.left is None:
            if len(answer) - 1 < index:
                answer.append([])
            answer[index] += [None]
        if node.right is not None:
            func1(node.right, answer, index)
        if node.right is None:
            if len(answer) - 1 < index:
                answer.append([])
            answer[index] += [None]

        return answer

    return func1(node1, answer=[], index=0) == func1(node2, answer=[], index=0)


def main():
    return 0


if __name__ == '__main__':
    node08 = Node(3)
    node07 = Node(4, node08)
    node06 = Node(4)
    node05 = Node(4)
    node04 = Node(4)
    node03 = Node(2, node06, node07)
    node02 = Node(2, node04, node05)
    node01 = Node(1, node02, node03)
    print(solution(node02, node03))
