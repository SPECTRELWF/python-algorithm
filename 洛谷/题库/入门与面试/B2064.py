'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-11-01 00:08:47
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2064.py
'''
n = int(input())
data = [1] * 31 
for i in range(2,31,1):
    data[i] = data[i-1] + data[i-2]
for i in range(n):
    a = int(input())
    print(data[a-1])
    