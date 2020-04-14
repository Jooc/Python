# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s += ' '
#         cur_word = ''
#         stack = []
#
#         for c in s:
#             print(c)
#             if c.isspace():
#                 if cur_word != '':
#                     stack.append(cur_word)
#                     stack.append(' ')
#                     cur_word = ''
#                 continue
#             else:
#                 cur_word = cur_word + c
#
#         print(stack)
#         ans = ''.join(stack[-2::-1])
#
#         return ans
#

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


demo = Solution()
print(demo.reverseWords("a good   example"))
