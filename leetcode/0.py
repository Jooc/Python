from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


q = PriorityQueue()


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

q.put((l1.val, l1))
q.put((l2.val, l2))
q.put((l3.val, l3))

while not q.empty():
    l, node = q.get()
    print(l)
