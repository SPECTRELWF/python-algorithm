s = input().strip()
tmp = s[::-1]
if tmp[0:2] == 're' or tmp[0:2] == 'yl':
    print(s[0:len(s) - 2:1])
elif tmp[0:3] == 'gni':
    print(s[0:len(s) - 3:1])
else:
    print(s)
