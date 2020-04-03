# from random import randint
#
# class Solution:
#     def randomized_partition(self, nums, left, right):
#         pivot = left
#         nums[pivot], nums[right] = nums[right], nums[pivot]
#         i = left - 1
#
#         for j in range(left, right):
#             if nums[j] < nums[right]:
#                 i += 1
#                 nums[j], nums[i] = nums[i], nums[j]
#
#         i += 1
#         nums[i], nums[right] = nums[right], nums[i]
#         print(nums[i], i, nums)
#
#         return i
#
#     def randomized_quicksort(self, nums, left, right):
#         if right - left <= 0:
#             return
#         mid = self.randomized_partition(nums, left, right)
#         self.randomized_quicksort(nums, left, mid - 1)
#         self.randomized_quicksort(nums, mid + 1, right)
#
#     def sortArray(self, nums):
#         self.randomized_quicksort(nums, 0, len(nums) - 1)
#         return nums
#
#
# demo = Solution()
# print(demo.sortArray([5,3,4,2,1]))