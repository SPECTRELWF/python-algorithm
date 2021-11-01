n = int(input())
data = list(map(int,input().split(' ')))
x = int(input())
pos = -1
for i in range(n):
    if data[i] == x:
        pos = i
        break
print(pos)