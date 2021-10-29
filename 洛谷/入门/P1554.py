m,n = map(int,input().split(" "))
res = [0]*10

def func(k):
    s = str(k)
    for c in s:
        res[int(c)] += 1
for i in list(range(m,n+1,1)):
    func(i)
for i in res:
    print(i,end=' ')
print()
