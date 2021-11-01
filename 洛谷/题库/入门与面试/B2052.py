'''
Author: lwf
Date: 2021-10-31 20:48:44
LastEditTime: 2021-10-31 23:24:26
LastEditors: lwf
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2052.py
'''
a , b , c = input().split(" ")

if c.strip() == '+':
    print(int(a) + int(b))
elif c.strip() == '-':
    print(int(a) - int(b))
elif c.strip() == '*':
    print(int(a) * int(b))
elif c.strip() == '/':
    if b.strip() == '0':
        print('Divided by zero!')
    else:
        print(int(a) + int(b))
else:
    print('Invalid operator!')