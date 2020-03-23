from collections import Counter

def majorityElement(nums: list) -> int:
    # size = len(nums)
    # kv = dict()
    #
    # ans = list()
    # for num in nums:
    #     if num in kv:
    #         kv[num] += 1
    #         if kv[num] > size/2:
    #             return num
    #     else:
    #         kv[num] = 1

    obj = Counter(nums)
    return obj.most_common(1)[0][0]


print(majorityElement([2,2,1,1,1,2,2]))