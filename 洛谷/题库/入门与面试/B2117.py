a = 'abcdefghijklmnopqrstuvwxyz'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input().strip())
for i in range(n):
    res = ''
    s = input().strip()
    if s[0] in a:
        res += A[a.index(s[0])]
    else:
        res += s[0]
    for c in range(1, len(s)):
        if s[c] in A:
            res += a[A.index(s[c])]
        else:
            res += s[c]
    print(res)
