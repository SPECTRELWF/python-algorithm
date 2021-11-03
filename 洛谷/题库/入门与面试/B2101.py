m, n = map(int, input().strip().split(' '))
data = [[0] * n] * m
for i in range(m):
    data[i] = list(map(int, input().strip().split(' ')))
res = 0
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == (m - 1) or j == (n - 1):
            res += data[i][j]
print(res)
