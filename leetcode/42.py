class Solution:
    def trap(self, height) -> int:
        size = len(height)
        if not size:
            return 0

        max_l, max_r = [0 for _ in range(size)], [0 for _ in range(size)]

        max_l[0] = height[0]
        for index in range(1, size):
            max_l[index] = max(height[index], max_l[index - 1])

        max_r[-1] = height[-1]
        for index in range(1, size):
            m_index = -1 * index
            max_r[m_index] = max(height[m_index], max_r[m_index + 1])

        ans = 0
        for index in range(1, size - 1):
            water = min(max_l[index], max_r[index]) - height[index]
            if water > 0:
                ans += water

        return ans


demo = Solution()
print(demo.trap([]))
