x , a , y , b = map(int,input().split(" "))

res = ((y*b)-(x*a))/(1.0*(b-a))
print("%.2f" % res)