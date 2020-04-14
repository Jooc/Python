class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()

            cur = a + b + carry
            carry = cur // 10
            cur %= 10

            curNode = ListNode(cur)
            curNode.next = ans
            ans = curNode

        return ans

def printL(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# printL(l1)
# printL(l2)

demo = Solution()
printL(demo.addTwoNumbers(l1, l2))
# printL(demo.addTwoNumbers(ListNode(5), ListNode(5)))



# class Solution:
#     def size(self, node) -> int:
#         res = 0
#         while node:
#             res += 1
#             node = node.next
#         return res
#
#     def carry(self, carried):
#         if carried.val == 9:
#             self.carry(self.carryStack.pop())
#             carried.val = 0
#         else:
#             carried.val = carried.val + 1
#
#     def add(self, cur, node1, node2):
#         print(node1.val, node2.val)
#         if node1.val + node2.val > 9:
#             self.carry(cur)
#             self.carryStack.clear()
#             cur.next = ListNode(node1.val + node2.val - 10)
#         else:
#             cur.next = ListNode(node1.val + node2.val)
#         self.carryStack.append(cur.next)
#         for i in range(len(self.carryStack)):
#             print(self.carryStack[i].val)
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         size1 = self.size(l1)
#         size2 = self.size(l2)
#
#         ans = ListNode(0)
#         cur_l1 = l1
#         cur_l2 = l2
#
#         self.carryStack = [ans]
#         # ans.next = ListNode(l1.val if size1 >= size2 else l2.val)
#
#         cur = ans
#         while size1 != size2:
#             if size1 > size2:
#                 self.add(cur, cur_l1, ListNode(0))
#                 cur, cur_l1 = cur.next, cur_l1.next
#                 size1 -= 1
#             else:
#                 self.add(cur, ListNode(0), cur_l2)
#                 cur, cur_l2 = cur.next, cur_l2.next
#                 size2 -= 1
#
#         while size1:
#             self.add(cur,cur_l1, cur_l2)
#             cur, cur_l1, cur_l2 = cur.next, cur_l1.next, cur_l2.next
#             size1 -= 1
#
#         return ans.next if ans.val == 0 else ans