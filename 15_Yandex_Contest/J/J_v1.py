def solution(node, index=0):
    index += 1
    if node.left is None and node.right is None:
        return index
    elif node.left is None:
        return max(index, solution(node.right, index))
    elif node.right is None:
        return max(index, solution(node.left, index))
    else:
        return max(index, solution(node.left, index), solution(node.right, index))