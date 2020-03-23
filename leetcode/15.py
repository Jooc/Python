def threeSum(nums: list) -> list:
    size = len(nums)
    if not nums or size < 3:
        return []

    ans = []
    nums.sort()

    for index in range(size):
        if nums[index] > 0:
            return ans

        L = index + 1
        R = size - 1

        if index > 0 and nums[index] == nums[index - 1]:
            continue

        while L < R:

            res = nums[index] + nums[L] + nums[R]
            if res == 0:
                ans.append([nums[index], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L-1] == nums[L]:
                    L += 1
                while L < R and nums[R+1] == nums[R]:
                    R += 1
            elif res > 0:
                R -= 1
            else:
                L += 1

    return ans

for row in threeSum([-4,0,0,2,2]):
    print(row)