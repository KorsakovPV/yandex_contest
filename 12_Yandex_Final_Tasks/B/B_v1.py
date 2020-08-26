def hasCycle(node):
    iter_step1 = iter_step2 = node
    while True:
        if iter_step2 is None or iter_step2.next is None:
            return False
        iter_step1 = iter_step1.next
        iter_step2 = iter_step2.next.next

        if iter_step1 == iter_step2:
            return True