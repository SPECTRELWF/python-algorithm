a, b = map(int, input().split(" "))

res = (a ** b) % 7

week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(week[res])
