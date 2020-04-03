from queue import Queue


class Solution:
    def maxDistance(self, grid) -> int:
        queue = Queue()
        n = len(grid)

        judge = 0
        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    judge += 1
                    queue.put((i, j))
        print('judge:', judge, ' q_size:', queue.qsize())

        if judge == n ** 2 or judge == 0:
            return -1

        distance = -1
        dire_x, dire_y = [0, 1, 0, -1], [-1, 0, 1, 0]
        while not queue.empty():
            distance += 1
            for _ in range(queue.qsize()):
                x, y = queue.get()
                for i in range(4):
                    cx, cy = x + dire_x[i], y + dire_y[i]
                    if 0 <= cx < n and 0 <= cy < n and grid[cx][cy] == 0:
                        print('cx=%d, cy=%d, distance=%d' % (cx, cy, distance))
                        grid[cx][cy] = 2
                        queue.put((cx, cy))

        return distance


demo = Solution()
print(demo.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
