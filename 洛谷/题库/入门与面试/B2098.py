n = int(input())
data = list(map(int,input().strip().split(' ')))
res = []
for i in data:
    if i not in res:
        res.append(i)
for j in res:
    print(j,end=' ')
print()