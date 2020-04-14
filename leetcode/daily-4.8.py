class Solution:
    def digit_sum(self, num):
        res = 0
        while num != 0:
            res += num % 10
            num = num // 10
        return res

    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        s = set()
        q.put((0, 0))

        grapth = [[0 for _ in range(n)] for _ in range(m)]

        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and x < m and y < n and self.digit_sum(x) + self.digit_sum(y) <= k:
                grapth[x][y] = 1
                s.add((x, y))
                for (dx, dy) in [(x + 1, y), (x, y + 1)]:
                    q.put((dx, dy))
            for i in range(m):
                print(grapth[i])
            print()

        return len(s)


demo = Solution()
# print(demo.digit_sum(3))
print(demo.movingCount(15, 15, 8))
