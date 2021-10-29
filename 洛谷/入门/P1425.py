a,b,c,d = map(int,input().split(" "))

if d < b :
    d += 60
    c -= 1
print(c-a,d-b)