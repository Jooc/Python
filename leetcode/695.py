def maxAreaOfIsland(grid: list) -> int:
    ans = 0
    for index_row, row in enumerate(grid):
        for index_col, col in enumerate(row):
            if grid[index_row][index_col] == 0:
                continue

            stack = [[index_row, index_col]]
            res = 1
            while stack:
                [cur_i, cur_j] = stack.pop()
                grid[cur_i][cur_j] = 0
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    i, j = cur_i + di, cur_j + dj
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                        continue
                    if grid[i][j] == 1:
                        res += 1
                        grid[i][j] = 0
                        stack.append([i, j])

            ans = max(ans, res)
    return ans


print(maxAreaOfIsland([[1,1,0,0,0],
       [1,1,0,0,0],
       [0,0,0,1,1],
       [0,0,0,1,1]]))

print(maxAreaOfIsland([[1]]))

