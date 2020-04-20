import collections


def updateMatrix(matrix) -> list:
    m, n = len(matrix), len(matrix[0])

    ans = [[0] * n for _ in range(m)]
    zeroes = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
    # print(zeroes)

    q = collections.deque(zeroes)
    seen = set(zeroes)

    direX, direY = [0, 1, 0, -1], [-1, 0, 1, 0]
    while q:
        x, y = q.popleft()
        for step in range(4):
            nx, ny = x + direX[step], y + direY[step]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx, ny))
                seen.add((nx, ny))

    return ans


# test = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
test = [[0,1,0], [1,1,1], [0,0,1]]
res = updateMatrix(test)

def printL(res):
    for i in range(len(res)):
        print(res[i])

printL(test)
print()
printL(res)



