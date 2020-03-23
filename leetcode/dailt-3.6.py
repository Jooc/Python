def findContinuousSequence(target: int) -> list:
    nums = list(range(1, target // 2 + 2))
    ans = list()

    begin = 0
    while begin < len(nums) - 1:
        end = begin + 1
        sum_single = nums[begin]

        while sum_single < target:
            sum_single += nums[end]
            end += 1

        if sum_single == target:
            ans.append(nums[begin:end])
        begin += 1

    return ans


for row in findContinuousSequence(9):
    print(row)
