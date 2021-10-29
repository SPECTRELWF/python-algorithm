n = int(input())
cnt = 0
res = 0
for  i in range(n):
    a,b = map(int,input().split(" "))
    res += cnt + (a + b) - 8
    cnt += (a + b) - 8
print(res)
