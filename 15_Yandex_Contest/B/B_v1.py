def solution(node):
    if node.left is None and node.right is not None:
        return False
    elif node.left is not None and node.right is None:
        return False
    elif node.left is None and node.right is None:
        return True
    else:
        return solution(node.left) and solution(node.right)