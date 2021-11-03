x = float(input())
res = 0
if x >= 10:
    res = x / 2 - 1.5
elif x >= 5:
    res = 2 - 1.5 * (x - 3) * (x - 3)
else:
    res = 2.5 - x
print('%.3f' % res)
