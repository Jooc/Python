def numberOfSubarrays(nums, k: int) -> int:
    size = len(nums)
    odd = [-1]
    for index in range(size):
        if nums[index] % 2 != 0:
            odd.append(index)
    odd.append(size)
    print(odd)

    ans = 0
    for i in range(1, len(odd) - k):
        ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])

    return ans


print(numberOfSubarrays([1, 1, 2, 1, 1], 3))
