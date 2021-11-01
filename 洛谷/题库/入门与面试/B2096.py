n = int(input())
data = list(map(int,input().strip().split(' ')))
maxx = max(data)
res = [0]*(maxx+1)
for i in data:
    res[i] += 1

for i in res:
    print(i)