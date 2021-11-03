s1 = input().strip()
n = len(s1)
res = ''
for i in range(n - 1):
    res += chr(ord(s1[i]) + ord(s1[i + 1]))
res += chr(ord(s1[0]) + ord(s1[n - 1]))
print(res)
