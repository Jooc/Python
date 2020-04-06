import collections

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def createList():
    head = Node(0)
    tail = Node(10)
    head.next = tail

    return head, tail


dd = collections.defaultdict(createList)
print(dd[1][0].key)
print(dd[10][-1].key)
print(dd[1].key)