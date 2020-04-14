class Soultion:

    def intersection(self, start1:[int], end1:[int], start2:[int], end2:[int]) -> list[float]:
        # 判断(xk,yk)是否在线段上
        # premise: (xk,yk) 已确定在直线上
        def inside(x1, y1, x2, y2, xk, yk):
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) \
                   and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        ans = []

        if (y4 - y3) * (x2 - x1) == (y2 - y1) * (x4 - x3):
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                if inside(x1, y1, x2, y2, x3, y3):
                    ans = update(ans, x3, y3)
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
        else:
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / (
                        (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / (
                        (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))

            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]

        return ans

demo = Soultion()
print(demo.intersection([0, 0], [1, 0], [1, 1], [0, -1]))
