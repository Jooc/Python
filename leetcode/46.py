import itertools


class Solution:
    def permute(self, nums) -> list:
        ans = []

        def backtrack(nums, tmp):
            if not nums:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return ans


demo = Solution()
print(demo.permute([1, 2, 3]))

#
# class Solution:
#     def permute(self, nums) -> list:
#         return list(itertools.permutations(nums))
