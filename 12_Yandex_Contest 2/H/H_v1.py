def solution(node):
    while node:
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            return node
        node = node.prev
