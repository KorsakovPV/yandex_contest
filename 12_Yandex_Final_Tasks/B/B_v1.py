# 33853958
def hasCycle(node):
    if type(node) != Node:
        return

    if node.next is None:
        return False

    iter_step1 = iter_step2 = node
    while iter_step2 is not None and iter_step2.next is not None:
        iter_step1 = iter_step1.next
        iter_step2 = iter_step2.next.next
        if iter_step1 == iter_step2:
            return True
    return False
