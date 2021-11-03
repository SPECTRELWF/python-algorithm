a,b,c = map(int,input().strip().split(' '))
m = 1.0*max(a,b,c)/(max(a+b,b,c)*max(a,b,b+c))
print('%.3f'%m)
