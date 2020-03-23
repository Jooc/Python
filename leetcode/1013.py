def canThreePartsEqualSum(A: list) -> bool:
    sum0 = 0
    for num in A:
        sum0 += num

    print(sum0)
    if sum0 % 3 != 0:
        return False

    sum1 = sum2 = sum3 = 0
    index = 0

    while index < len(A):
        sum1 += A[index]
        index += 1
        if sum1 == sum0 / 3:
            break

    while index < len(A):
        sum2 += A[index]
        index += 1
        if sum2 == sum0 / 3:
            break

    if index >= len(A):
        return False
    while index < len(A):
        sum3 += A[index]
        index += 1
        if sum3 == sum0 / 3:
            break

    print(sum1,sum2,sum3)
    if sum1 == sum2 == sum3 == sum0 / 3:
        return True
    else:
        return False


print(canThreePartsEqualSum([1,-1,1,-1]))