n = int(input())
data = [1] * 16
for i in range(2,16):
    data[i] = data[i-1] * i
res = 1.0
for i in range(1,n+1):
    res += 1.0/data[i]
print('%.10f' % res)