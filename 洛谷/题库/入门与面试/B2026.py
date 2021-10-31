a,b = map(float,input().split(" "))
res = int(a / b)

res = a - res*b
print("%.6f " % res)