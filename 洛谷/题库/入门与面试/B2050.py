a, b, c = map(int, input().split(" "))

if a + b < c or a + c < b or b + c < a:
    print('0')
else:
    print('1')
