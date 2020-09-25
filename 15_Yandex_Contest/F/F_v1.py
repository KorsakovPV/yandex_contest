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