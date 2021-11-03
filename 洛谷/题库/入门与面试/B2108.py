n, m = map(int, input().strip().split(' '))
img1 = [[0] * m] * n
for i in range(n):
    img1[i] = list(map(int, input().strip().split(' ')))
res = 0
for i in range(n):
    for j in range(m):
        if i == 0 or i == (n - 1) or j == (m - 1) or j == 0:
            res = img1[i][j]
        else:
            res = (img1[i][j] + img1[i - 1][j] + img1[i + 1][j] + img1[i][j - 1] + img1[i][j + 1])
            res /= 5.0

            res = int(round(res))
        print(res, end=' ')
    print()
