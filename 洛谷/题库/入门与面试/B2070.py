'''
Author: your name
Date: 2021-10-31 20:48:43
LastEditTime: 2021-11-01 00:26:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2070.py
'''
n = int(input())
res = 0.0
for i in range(1,n+1,1):
    res += ((-1)**(i-1))*(1.0/i)

print("%.4f" % res)