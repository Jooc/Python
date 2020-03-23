class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        heads = []
        for list_head in lists:
            heads.append(list_head)

        cur = sentry = ListNode(0)
        flag = True

        while flag:
            flag = False
            for head in heads:
                if head:
                    flag = True
                    break
            if not flag:
                break

            next_head = None
            next_index = -1
            val = float('inf')

            for i in range(len(heads)):
                if heads[i]:
                    if heads[i].val < val:
                        val = heads[i].val
                        next_index = i

            print(next_index)
            cur.next = heads[next_index]
            heads[next_index] = heads[next_index].next
            cur = cur.next

        return sentry.next


i1 = ListNode(1)
i1.next = ListNode(4)
i1.next.next = ListNode(5)

i2 = ListNode(1)
i2.next = ListNode(3)
i2.next.next = ListNode(4)

i3 = ListNode(2)
i3.next = ListNode(6)

l123 = [i1, i2, i3]

demo = Solution()
result = demo.mergeKLists(l123)

while result:
    print('res', result.val)
    result = result.next

