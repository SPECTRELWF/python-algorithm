n = int(input())
if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
    print('3 5 7')
elif n % 3 == 0 and n % 5 == 0:
    print('3 5')
elif n % 3 == 0 and n % 7 == 0:
    print('3 7')
elif n % 5 == 0 and n % 7 == 0:
    print('5 7')
elif n % 3 == 0:
    print('3')
elif n % 5 == 0:
    print('5')
elif n % 7 == 0:
    print('7')
else:
    print("n")
