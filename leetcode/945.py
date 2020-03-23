class Solution:
    def minIncrementForUnique(self, A: list) -> int:
        # count = set()
        #
        # move = 0
        # for num in A:
        #     while num in count:
        #         num += 1
        #         move += 1
        #     count.add(num)
        #
        # return move
        A.sort()
        print(A)
        count = 0
        for index in range(1, len(A)):
            print(A)
            if A[index] <= A[index - 1]:
                count += (A[index - 1] - A[index] + 1)
                A[index] = A[index - 1] + 1

        print(A)
        return count


demo = Solution()
print(demo.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
