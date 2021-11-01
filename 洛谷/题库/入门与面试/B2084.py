n = int(input())

for i in range(3,n,1):
    if n % i == 0:
        print(max(i,int(n/i)))
        break