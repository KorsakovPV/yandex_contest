"""
D. Дерево - анаграмма

Кондратий приказал найти в его лесу дерево - анаграмму. Гоша и Алла отправились
 на поиски. Помогите ребятам определить, является ли дерево, которое они нашли
 деревом - анаграммой?

Дерево является анаграммой, если оно симметричное относительно своего центра.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def solution1(node):
    def func1(node, answer=[], index=0):
        if len(answer) - 1 < index:
            answer.append([])
        answer[index] += [node.value]
        index += 1
        if node.left is not None:
            func1(node.left, answer, index)
        if node.right is not None:
            func1(node.right, answer, index)
        return answer

    for level in func1(node, answer=[], index=0):
        for i in range(len(level) // 2):
            if level[i] != level[-i - 1]:
                return False
    return True

def mirror_tree(a, b):
    if a is None and b is None:
        return True
    if a and b:
        return (
                a.value == b.value and
                mirror_tree(a.left, b.right) and
                mirror_tree(a.right, b.left)
        )
    return False
def solution(node):
    a = node.left
    b = node.right
    return mirror_tree(a, b)

def main():
    return 0


if __name__ == '__main__':
    node07 = Node(4)
    node06 = Node(3)
    node05 = Node(3)
    node04 = Node(4)
    node03 = Node(2, node06, node07)
    node02 = Node(2, node04, node05)
    node01 = Node(1, node02, node03)
    x = node01
    print(solution(x))
    print(solution1(x))

# if __name__ == "__main__":
#     root = Node(15)
#     root.left = Node(19)
#     root.right = Node(19)
#     root.left.left = Node(11)
#     root.left.right = Node(11)
#     print(solution(root))