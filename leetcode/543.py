# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = 0

        def depth(node) -> int:
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)

            self.ans = max(self.ans, L+R)
            return max(L, R) + 1

        depth(root)
        return self.ans


sol = Solution()

tree = TreeNode(x=1)
tree.left = TreeNode(x=2)
tree.right = TreeNode(x=3)
tree.left.left = TreeNode(x=4)
tree.left.right = TreeNode(x=5)

print(sol.diameterOfBinaryTree(tree))
