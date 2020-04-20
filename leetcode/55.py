def canJump(nums) -> bool:
    n = len(nums)
    farest = 0

    for i in range(n):
        if i <= farest:
            farest = max(farest, i + nums[i])
            if farest > n:
                return True

    return False


print(canJump([2,1,1,0,4]))