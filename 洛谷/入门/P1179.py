l , r  = map(int,input().split(" "))
res = 0
for i in range(r-l+1):
    s = str(i+l)
    res += s.count('2')
print(res)