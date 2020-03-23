class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums:
            return None

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(nums[left], nums[right], nums[mid])

            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


demo = Solution()
print(demo.search([3, 1], 1))
