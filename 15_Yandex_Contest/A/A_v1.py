def solution(node):
    if node.left is None and node.right is None:
        return node.value
    if node.left is None and node.right is not None:
        return max(node.value, solution(node.right))
    if node.left is not None and node.right is None:
        return max(node.value, solution(node.left))
    return max(node.value, solution(node.left), solution(node.right))