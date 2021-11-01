price = [28.9,32.7,45.6,78,35,86.2,27.8,43,56,65]
res = 0
num = list(map(int,input().strip().split(' ')))

for i in range(10):
    res += price[i]*num[i]
print('%.1f' % res)