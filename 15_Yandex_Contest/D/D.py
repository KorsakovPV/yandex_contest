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


def solution(node):
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


def main():
    return 0


if __name__ == '__main__':
    node07 = Node(4)
    node06 = Node(4)
    node05 = Node(4)
    node04 = Node(4)
    node03 = Node(2, node06, node07)
    node02 = Node(2, node04, node05)
    node01 = Node(1, node02, node03)
    print(solution(node01))
