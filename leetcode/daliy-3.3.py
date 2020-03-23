import collections


def orangesRotting(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])

    queue = collections.deque()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 2:
                queue.append((r, c, 0))

    def iterator_def(r, c):
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < R and 0 <= c < C:
                yield nr, nc

    d = 0
    while queue:
        r, c, d = queue.popleft()
        for nr, nc in iterator_def(r, c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr, nc, d + 1))

    for row in grid:
        for cell in row:
            if cell == 1:
                return -1

    return d

print()