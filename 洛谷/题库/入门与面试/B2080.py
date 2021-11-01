x, n = input().split(' ')
x = float(x)
n = int(n)

res = 1.0

for i in range(1, n + 1, 1):
    res += (x ** i)

print('%.2f' % res)
