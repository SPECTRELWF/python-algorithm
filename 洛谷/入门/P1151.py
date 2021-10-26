k = int(input(""))

def func(i,k):
    a = int(str(i)[0:3])
    b = int(str(i)[1:4])
    c = int(str(i)[2:5])
    if a % k == 0 and b % k == 0 and c % k == 0:
        return True
res = 0
for i in range(20001):
    if(func(i+10000,k)):
        res+=1
        print(i+10000) 
if res == 0:
    print("No")

