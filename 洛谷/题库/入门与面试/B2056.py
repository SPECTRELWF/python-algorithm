'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-10-31 23:47:53
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2056.py
'''
n = int(input())
res = 0
for i in range(n):
    num = int(input())
    res += num
print(res,end=' ')
print("%.5f" % (res/(n*1.0)))