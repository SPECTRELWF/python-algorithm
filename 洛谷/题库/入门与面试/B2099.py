data = [[],[],[],[],[]]
for i in range(5):
    data[i] = list(map(int,input().strip().split(' ')))
m , n = map(int,input().strip().split(' '))
data[m-1],data[n-1] = data[n-1], data[m-1]
for i in range(5):
    for j in range(5):
        print(data[i][j],end=' ')
    print()