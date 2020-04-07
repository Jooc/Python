# O(n^2) O(1)
class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

        for i in range(n):
            print(matrix[i])
        print()

        for i in range(n):
            for j in range(i):
                print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            print(matrix[i])


# O(n^2) O(n^2)
# class Solution:
#     def rotate(self, matrix) -> None:
#         n = len(matrix)
#         res = [[0 for _ in range(n)] for _ in range(n)]
#
#         for i in range(n):
#             for j in range(n):
#                 res[j][n - 1 - i] = matrix[i][j]
#
#         return res


demo = Solution()
print(demo.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(demo.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
