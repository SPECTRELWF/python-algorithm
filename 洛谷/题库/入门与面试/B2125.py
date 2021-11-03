n = int(input())
score = []
name = []
for i in range(n):
    a, b = input().strip().split(' ')
    score.append(int(a))
    name.append(b)
print(name[score.index(max(score))])
