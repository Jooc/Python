from random import randint


class Solution:
    def partition(self, nums, left, right):
        pivot = randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]

        i = left - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        i += 1
        nums[i], nums[right] = nums[right], nums[i]

        return i

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def sortArray(self, nums) -> list:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums


demo = Solution()
print(demo.sortArray([5, 4, 2, 3, 1]))
