n = int(input())
res = [1]*(n+1)
def reverse(k):
    if k == 0:
        return 1
    else:
        return 0
def func(i,n):
    for j in range(1,n+1):
        if j % i == 0:
            res[j] = reverse(res[j])
for i in range(1,n+1):
    func(i, n)

for i in range(1,n+1):
    if res[i] == 0:
        print(i,end=" ")
print()