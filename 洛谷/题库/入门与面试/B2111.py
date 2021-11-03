n = float(input().strip())
s1 = input().strip()
s2 = input().strip()
res = 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        res += 1
if 1.0 * res / len(s1) > n:
    print('yes')
else:
    print('no')
