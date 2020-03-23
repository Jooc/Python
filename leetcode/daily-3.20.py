# Sequence
import heapq

class Solution:
    def getLeastNumbers(self, arr: list, k: int) -> list:
        hp = arr[:5]
        heapq.heapify(hp)

        print(hp)

demo = Solution()
print(demo.getLeastNumbers([5,1,2,1,3,4,0], 3))