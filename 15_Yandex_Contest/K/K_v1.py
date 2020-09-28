def solution(node, numeral=0, amount=0):
    numeral = numeral * 10 + node.value
    if node.left is None and node.right is None:
        return amount + numeral
    elif node.left is None:
        return solution(node.right, numeral, amount)
    elif node.right is None:
        return solution(node.left, numeral, amount)
    else:
        return solution(node.left, numeral, amount)+solution(node.right, numeral, amount)