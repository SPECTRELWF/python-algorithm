s = input().strip().split(' ')
for i in s[0:len(s) - 1]:
    if len(i.strip()) != 0:
        print(len(i.strip()), end=',')
print(len(s[len(s) - 1]))
