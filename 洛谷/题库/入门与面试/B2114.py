s = input().strip()
for i in s:
    if i == 'A':
        print('T', end='')
    if i == 'T':
        print('A', end='')
    if i == 'C':
        print('G', end='')
    if i == 'G':
        print('C', end='')
