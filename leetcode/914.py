import collections
import functools
import math


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        count = collections.Counter(deck)
        vals = functools.reduce(math.gcd, count.values())
        return vals >= 2

# class Solution:
#     def hasGroupsSizeX(self, deck) -> bool:
#         count = collections.Counter(deck)
#         N = len(deck)
#
#         for x in range(2, N + 1):
#             if N % x == 0:
#                 if all(v % x == 0 for v in count.values()):
#                     return True
#
#         return False


demo = Solution()
print(demo.hasGroupsSizeX([1]))
