'''
Author: liuweifeng
Date: 2021-10-31 20:48:44
LastEditTime: 2021-10-31 23:37:13
LastEditors: liuweifeng
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2054.py
'''
n = int(input())
res = 0
for i in range(n):
    age = int(input())
    res += age
print("%.2f"%(res*1.0/n))