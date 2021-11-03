s = input().strip()
res = 0
for i in s:
    if i in '0123456789':
        res += 1
print(res)
