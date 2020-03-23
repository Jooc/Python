import queue


class MaxQueue:
    def __init__(self):
        self.queue = queue.deque()
        self.sort_queue = queue.deque()

    def max_value(self) -> int:
        if self.sort_queue:
            return self.sort_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.sort_queue and self.sort_queue[-1] <= value:
            self.sort_queue.pop()
        self.sort_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        ans = self.queue.popleft()
        if ans == self.sort_queue[0]:
            self.sort_queue.popleft()

        return ans


queue = MaxQueue()
queue.pop_front()
queue.pop_front()
queue.pop_front()
queue.push_back(15)
queue.push_back(9)
print(queue.max_value())
print(queue.pop_front())

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
