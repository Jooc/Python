class Solution:
    def numRookCaptures(self, board: list) -> int:
        ans = 0
        Rx = Ry = 0
        direx, direy = [0, 1, 0, -1], [1, 0, -1, 0]

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'R':
                    Rx, Ry = i, j

        for i in range(4):
            step = 0
            while True:
                cx = Rx + step * direx[i]
                cy = Ry + step * direy[i]
                if cx < 0 or cx >= 8 or cy < 0 or cy >= 8 or board[cx][cy] == 'B':
                    break
                if board[cx][cy] == 'p':
                    ans += 1
                    break
                step += 1

        return ans

demo = Solution()
print(demo.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))

