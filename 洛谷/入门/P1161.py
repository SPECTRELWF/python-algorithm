data = [0] * 2000001
# print(a)

def key(k):
    if k == 0:
        return 1
    else:
        return 0

n = int(input(""))
for i in range(n):
    a,t = input().split(" ")
    a = float(a)
    t = int(t)
    for j in range(t):
        data[int((j+1)*a)] = key(data[int((j+1)*a)])
print(data.index(1))

