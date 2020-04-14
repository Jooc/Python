class Solution:
    def generateParenthesis(self, n: int) -> list:
        ans = []
        cur_str = ''

        self.return_times = 0

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                ans.append(cur_str)

                self.return_times += 1
                print(cur_str, self.return_times)

                return
            if right < left:
                self.return_times += 1
                print(cur_str, self.return_times)

                return

            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return ans


# bad BFS
# class Solution:
#     def generateParenthesis(self, n: int) -> list:
#         from queue import Queue
#         q = Queue()
#         res = []
#
#         height = 1
#         q.put(('()', height))
#
#         while not q.empty():
#             cur, height = q.get()
#             out, left, right = '(' + cur + ')', '()' + cur, cur + '()'
#
#             if cur == ''
#
#             for s in [out, left, right]:
#                 if s not in res and height <= n - 1:
#                     q.put((s, height + 1))
#                     if height == n - 1:
#                         res.append(s)
#
#         return res


demo = Solution()
print(demo.generateParenthesis(3))
