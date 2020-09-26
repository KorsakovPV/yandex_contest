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