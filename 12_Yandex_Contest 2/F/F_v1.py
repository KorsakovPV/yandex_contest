def solution(node, index):
    head = node

    if index == 0:
        return node.next_item

    while index - 1:
        node = node.next_item
        index -= 1

    node.next_item = node.next_item.next_item
    return head
