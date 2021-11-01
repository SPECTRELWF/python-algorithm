'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-11-01 00:05:59
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2063.py
'''
x,n = map(int,input().split(' '))
res = x * (1.001**n)
print('%.4f' % res)