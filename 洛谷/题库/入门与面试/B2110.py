s = input().strip()
flag = 0
for i in s:
    if s.count(i) == 1:
        flag = 1
        print(i)
        break
if flag == 0:
    print('no')
