'''
Author: your name
Date: 2021-10-31 20:48:43
LastEditTime: 2021-11-01 00:37:06
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2075.py
'''
a,b = map(int,input().split(' '))
res = str(a ** b)

if len(res) < 3:
    print('0'*(3-len(res)) + res)
else:
    res = res[::-1]
    print(res[0:3][::-1])