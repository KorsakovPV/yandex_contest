INT_MAX = 4294967296

INT_MIN = -4294967296

def solution(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

def isBSTUtil(node, mini, maxi):

    if node is None:
        return True

    if node.value < mini or node.value > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.value - 1) and
            isBSTUtil(node.right, node.value + 1, maxi))