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