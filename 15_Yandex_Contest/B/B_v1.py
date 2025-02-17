def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def solution(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (abs(lh - rh) <= 1) and solution(root.left) is True and solution(
            root.right) is True:
        return True
    return False