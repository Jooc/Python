class TrieNode:
    def __init__(self, depth):
        self.depth = depth
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words) -> TrieNode:
        root = TrieNode(0)

        for word in words:
            t_word = word[::-1]

            cur = root
            depth = root.depth + 1

            for ch in t_word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode(depth)

                cur = cur.children[ch]
                depth += 1

        stack = [root]
        ans = 0
        while stack:
            cur = stack.pop()
            if len(cur.children.keys()) == 0:
                ans += cur.depth + 1
            for node in cur.children.values():
                stack.append(node)

        return ans


demo = Solution()
print(demo.minimumLengthEncoding(["time", "me", "bell"]))
