data = list(map(int, input().strip().split(" ")))
eat = 0
data[1] += data[0] // 3
data[4] += data[0] // 3
eat += data[0] % 3
data[0] = data[0] // 3

for i in range(1, 4, 1):
    eat += data[i] % 3
    data[i - 1] += data[i] // 3
    data[i + 1] += data[i] // 3
    data[i] = data[i] // 3

data[0] += data[4] // 3
data[3] += data[4] // 3
eat += data[4] % 3
data[4] = data[4] // 3

for i in range(5):
    print(str(data[i]), end=' ')
print()
print(str(eat))
