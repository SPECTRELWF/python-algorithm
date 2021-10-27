s1 = input()
s2 = input()

res1 = 1
for i in s1:
    res1 *= ord(i)-ord('A') + 1

##ORD求字符的asici码值
res2 = 1
for i in s2:
    res2 *= ord(i)-ord('A') + 1

if res1 % 47 == res2 % 47:
    print("GO")
else:
    print("STAY")