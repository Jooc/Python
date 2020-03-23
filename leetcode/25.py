class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        sentry = ListNode(0)
        pre = sentry
        start = head
        flag = True
        while head:
            for _ in range(k):
                if not head:
                    flag = False
                    break
                head = head.next
            if not flag:
                break

            pre.next = self.reverse(start, head)
            start.next = head
            pre = start
            start = head
        return sentry.next

    def reverse(self, start, end):
        pre, cur, nexts = None, start, start
        while cur != end:
            nexts = nexts.next
            cur.next = pre
            pre = cur
            cur = nexts
        return pre


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

demo = Solution()
l = demo.reverseKGroup(a, 2)

while l:
    print(l.val)
    l = l.next



# Stack
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         stack = []
#         res = cur = None
#         while head:
#             for _ in range(k):
#                 if not head:
#                     while stack:
#                         cur.next = stack.pop()
#                         cur = cur.next
#                     return res
#                 stack.append(head)
#                 head = head.next
#             while stack:
#                 if not res:
#                     temp = stack.pop()
#                     temp.next = None
#                     res = temp
#                     cur = res
#                     # print(res.val, cur.val)
#                 else:
#                     temp = stack.pop()
#                     temp.next = None
#                     cur.next = temp
#                     cur = cur.next
#
#         return res