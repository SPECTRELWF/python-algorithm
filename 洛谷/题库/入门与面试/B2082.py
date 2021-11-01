l , r = map(int,input().strip().split(' '))
res = 0
for i in range(l,r+1,1):
    res += str(i).strip().count('2')
print(res)
