n = int(input())
s = input().split(" ")
data = list(map(int,s))
data = list(set(data))

data.sort()

print(len(data))
for i in range(len(data)):
    print(data[i],end=" ")
print()