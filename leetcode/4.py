def findMedianSortedArrays(nums1, nums2) -> float:
    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp
    size1, size2 = len(nums1), len(nums2)

    if size1 == 0:
        return (nums2[(size2 + 1) // 2] + nums2[(size2 + 2) // 2]) / 2

    k1, k2 = (size1 + size2 + 1) // 2, (size1 + size2 + 2) // 2
    print(k1, k2)

    index1 = index2 = 0

    while True:
        





print(findMedianSortedArrays([1,3],[2]))