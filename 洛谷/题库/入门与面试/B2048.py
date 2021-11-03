x, c = input().strip().split(" ")
res = 0
x = int(x)

if x <= 1000:
    res = 8
else:
    x -= 1000
    res = 8 + (int(x / 500)) * 4
    if x % 500 != 0:
        res += 4

if c == 'y':
    res += 5
print(res)
