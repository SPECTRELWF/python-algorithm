x = float(input())
res = 0
start = 2
dist = 0
while(True):
    dist += start
    res += 1
    start *= 0.98
    if dist > x:
        break
print(res) 