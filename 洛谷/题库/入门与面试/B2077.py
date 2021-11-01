n = int(input())
while n != 1:
    if n % 2 == 1:
        print(int(n),end="")
        print('*3+1=',end='')
        n = n*3+1
        print(int(n))
    else:
        print(n,end='')
        print('/2=',end='')
        n /= 2
        n = int(n)
        print(n)
print('End')
