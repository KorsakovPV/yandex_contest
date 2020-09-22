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

