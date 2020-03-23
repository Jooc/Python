left = [1 for _ in range(10)]

print(left)

for i in range(len(left) - 2, -1, -1):
    left[i] = 0

print(left)