import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


demo = Solution()
print(demo.findKthLargest([3, 2, 1, 5, 6, 4], 2))
