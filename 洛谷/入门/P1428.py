n = int(input())
data = list(map(int,input().split(" ")))
for i in range(len(data)):
    if i == 0:
        print(0,end=' ')
    else:
        res = 0
        for j in range(i):
            if data[j] < data[i]:
                res += 1
        print(res,end=' ')
print()