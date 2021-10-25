s = input().split(" ")
h = int(input())
h += 30
res = 0
for i in s:
    if int(i) <= h:
        res += 1
print(res)