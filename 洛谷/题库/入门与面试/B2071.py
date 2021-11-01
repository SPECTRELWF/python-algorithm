'''
Author: your name
Date: 2021-10-31 20:48:43
LastEditTime: 2021-11-01 00:28:18
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2071.py
'''
a,b,c = map(int,input().split(' '))
for i in range(2,a):
    if a % i == b % i and a % i == c % i:
        print(i)
        break