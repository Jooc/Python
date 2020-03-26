class Solution:
    def surfaceArea(self, grid: list) -> int:
        area = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] > 0:
                    area += 2
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(row):
                        area += max(grid[ni][nj] - grid[i][j], 0)
                    else:
                        area += grid[i][j]
                print('[%d][%d] added: %d' % (i, j, area))

        return area


demo = Solution()
print(demo.surfaceArea([[1, 0], [0, 2]]))
