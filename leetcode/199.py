from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 栈 - 深搜
class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        maxDepth = -1
        stack = [(root, 0)]
        ans = dict()

        while stack:
            (node, depth) = stack.pop()

            if node is not None:
                maxDepth = max(maxDepth, depth)
                ans.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [ans[depth] for depth in range(maxDepth + 1)]



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

demo = Solution()
print(demo.rightSideView(root))




# 队列 - 层序遍历
# class Solution:
#     def rightSideView(self, root: TreeNode) -> list:
#         q = Queue()
#         maxDepth = -1
#
#         ans = dict()
#
#         q.put((root, 0))
#         while not q.empty():
#             (node, depth) = q.get()
#
#             if node is not None:
#                 maxDepth = max(maxDepth, depth)
#
#                 ans[depth] = node.val
#
#                 q.put((node.left, depth + 1))
#                 q.put((node.right, depth + 1))
#
#         return [ans[depth] for depth in range(maxDepth + 1)]