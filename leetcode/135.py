class Solution:
    def candy(self, ratings: list) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]

        for index in range(1, len(ratings)):
            print(index)
            if ratings[index] > ratings[index - 1]:
                left[index] = left[index - 1] + 1

        print()

        for index in range(len(ratings) - 2, -1, -1):
            print(index)
            if ratings[index] > ratings[index + 1]:
                right[index] = right[index + 1] + 1

        print()
        print(left, right)

        ans = 0
        for index in range(len(ratings)):
            ans += (max(left[index], right[index]))

        return ans


demo = Solution()
print(demo.candy([1, 0, 2]))
