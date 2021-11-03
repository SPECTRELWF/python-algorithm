s = input().strip()
a = 'abcdefghijklmnopqrstuvwxyz'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''
for i in s:
    if i in a:
        res += A[a.index(i)]
    if i in A:
        res += a[A.index(i)]
res = res[::-1]
key = ''
for i in res:
    if i in a:
        key += a[(a.index(i) + 3) % 26]
    if i in A:
        key += A[(A.index(i) + 3) % 26]
print(key)
