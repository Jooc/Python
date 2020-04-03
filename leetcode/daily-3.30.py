class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))

        index = 0
        while len(nums) > 1:
            index = (index + m - 1) % len(nums)
            print(nums[index])
            nums.pop(index)
            print(nums)

        return nums[0]


demo = Solution()
print('remain', demo.lastRemaining(5, 3))
