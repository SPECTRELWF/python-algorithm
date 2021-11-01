'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-10-31 23:56:41
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2060.py
'''
m , n = map(int,input().split(' '))

res = 0
for i in range(m,n+1,1):
    if i % 17 == 0:
        res += i
print(res) 