n = int(input())
data = list(map(int,input().strip().split(' ')))
res = 0
cnt = 1

for i in range(1,n):
    res = max(res, cnt)
    if data[i] == data[i-1]:
        cnt += 1
    else:
        cnt = 1
print(res)