m, n = map(int, input().strip().split(' '))
img1 = [[0] * n] * m
for i in range(m):
    img1[i] = list(map(int, input().strip().split(' ')))

for i in range(n):
    for j in range(m):
        print(img1[j][i], end=' ')
    print()
