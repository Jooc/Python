class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        direX, direY = [-1, 0, 1, 0], [0, -1, 0, 1]

        def dfs(x, y):
            grid[x][y] = res
            for step in range(4):
                nx, ny = x + direX[step], y + direY[step]
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == '1':
                        dfs(nx, ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        printL(grid)

        return res


def printL(l):
    for i in range(len(l)):
        print(l[i])
    print()


demo = Solution()
print(demo.numIslands([["1","1","1"],
                       ["0","1","0"],
                       ["1","1","1"]]))

# class Solution:
#     def numIslands(self, grid) -> int:
#         m, n = len(grid), len(grid[0])
#
#         res = [[1 if (i == 0 or j == 0) and grid[i][j] == '1' else 0 for j in range(n)] for i in range(m)]
#         # printL(res)
#
#         islandNum = 1
#
#         direX, direY = [-1, 0], [0, -1]
#         for x in range(1, m):
#             for y in range(1, n):
#                 if grid[x][y] == '1':
#                     ux, uy = x + direX[0], y + direY[0]
#                     lx, ly = x + direX[1], y + direY[1]
#
#                     if res[ux][uy] == res[lx][ly] == 0:
#                         pass
#                     if res[ux][uy] != 0 and res[lx][ly] != 0:
#
#
#         printL(res)
