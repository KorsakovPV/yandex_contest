class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

    def __str__(self):
        return self.value

def solution_print(node):
    while node:
        print(node)
        node = node.next_item

def solution(node, index):
    head = node

    if index == 0:
        return node.next_item

    while index-1:
        node = node.next_item
        index -= 1

    node.next_item = node.next_item.next_item
    return head

def insert_node(node, index, value):
    head = node
    new_node = Node(value)
    if index == 0:
        new_node.next = node
        return new_node
    while index-1:
        node = node.next
        index -= 1
    tmp = node.next
    node.next = new_node
    new_node.next = tmp
    return head




n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

node_first = Node('first')
node = node_first

for i in range(4):
    node.next_item = Node(str(i)*5)
    node = node.next_item

solution_print(node_first)
print()
solution_print(solution(node_first, 0))
