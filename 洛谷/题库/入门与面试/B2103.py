m, n = map(int, input().strip().split(' '))
img1 = [[0] * n] * m
img2 = [[0] * n] * m
res = 0
for i in range(m):
    img1[i] = list(map(int, input().strip().split(' ')))
for i in range(m):
    img2[i] = list(map(int, input().strip().split(' ')))
for i in range(m):
    for j in range(n):
        if img1[i][j] == img2[i][j]:
            res += 1
print('%.2f' % (res * 100.0 / (m * n)))
