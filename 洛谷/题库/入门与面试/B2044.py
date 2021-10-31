a , b , c = map(int,input().split(" "))
cnt = 0
if a < 60:
    cnt += 1 
if b < 60:
    cnt += 1 
if c < 60:
    cnt += 1 

if cnt == 1:
    print("1")
else:
    print("0")