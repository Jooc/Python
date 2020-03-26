class Solution:
    def massage(self, nums: list):
        size = len(nums)
        if not size:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, size):
            tdp0 = max(dp0, dp1)
            tdp1 = dp0 + nums[i]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)


demo = Solution()
print(demo.massage([2, 1, 4, 5, 3, 1, 1, 3]))
