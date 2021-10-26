res = 0
maxs = 0
for i in range(7):
    a,b = map(int,input().split(" "))
    if a + b > maxs:
        maxs = a + b
        res = i + 1
if maxs > 8:
    print(res)
else:
    print(0)