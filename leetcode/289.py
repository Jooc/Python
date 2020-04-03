class Solution:
    def gameOfLife(self, board: [[]]) -> None:
        now = []
        for i in range(len(board)):
            now.append(list(board[i]))

        dirX = [-1, 0, 1, 1, 1, 0, -1, -1]
        dirY = [-1, -1, -1, 0, 1, 1, 1, 0]

        n = len(now)
        for x in range(n):
            for y in range(len(now[x])):
                live = 0
                for i in range(8):
                    posx, posy = x + dirX[i], y + dirY[i]
                    if 0 <= posx < n and 0 <= posy < len(now[posx]):
                        if now[posx][posy] == 1:
                            print(x, y, posx, posy)
                            live += 1
                print('x: %d, y: %d, live: %d' % (x, y, live))
                if now[x][y] == 1:
                    if live < 2 or live > 3:
                        board[x][y] = 0
                else:
                    if live == 3:
                        board[x][y] = 1


test = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
demo = Solution()
demo.gameOfLife(test)

print(test)
