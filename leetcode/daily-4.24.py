class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)

        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        while i <= mid:
            tmp[pos] = nums[i]
            count += (j - (mid + 1))
            pos += 1
            i += 1

        while j <= r:
            tmp[pos] = nums[j]
            pos += 1
            j += 1

        nums[l:r + 1] = tmp[l:r + 1]
        return count

    def reversePairs(self, nums) -> int:
        size = len(nums)
        tmp = [0] * size
        return self.mergeSort(nums, tmp, 0, size - 1)


demo = Solution()
print(demo.reversePairs([1,3,2,3,1]))
