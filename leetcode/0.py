test = [
    [0, 1, 0],
    [0, 0, 1],
]

now = []
for i in range(len(test)):
    now.append(list(test[i]))

print(test)
print(now)

test[0][0] = 1
print(test)
print(now)
