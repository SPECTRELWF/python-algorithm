x , n = map(int,input().split(" "))

res = 0

for i in range(n):
    if x!=6 and x!= 7:
        res += 250
    if x == 7:
        x = 1
    else:
        x += 1
print(res)