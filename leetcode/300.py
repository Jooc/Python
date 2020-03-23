def lengthOfLIS(nums: list) -> int:
    # if not nums:
    #     return 0
    #
    # size = len(nums)
    # dp = [1] * size
    # for i in range(size):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j]+1)
    #
    # print(dp)
    # return max(dp)

    d = []
    for num in nums:
        if not d or num > d[-1]:
            d.append(num)
        else:
            l, r = 0, len(d) - 1

            loc = r
            while l <= r:
                mid = (l+r)//2
                if d[mid] > num:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = num
    print(d)
    return len(d)



print(lengthOfLIS([18,55,66,2,3,54]))