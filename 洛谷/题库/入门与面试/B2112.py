n = int(input().strip())
for i in range(n):
    s1, s2 = input().strip().split(' ')
    if s1 == s2:
        print('Tie')
    elif s1 == 'Rock' and s2 == 'Scissors' or s1 == 'Scissors' and s2 == 'Paper' or s1 == 'Paper' and s2 == 'Rock':
        print('Player1')
    else:
        print('Player2')
