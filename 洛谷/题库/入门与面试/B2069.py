'''
Author: your name
Date: 2021-10-31 20:48:43
LastEditTime: 2021-11-01 00:23:00
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2069.py
'''
n = int(input())
seq1 = [0] * 31
seq2 = [0] * 31
seq1[0] = 2.0
seq2[0] = 1.0
seq1[1] = 3.0
seq2[1] = 2.0
for i in range(2,31,1):
    seq1[i] = seq1[i-1] + seq1[i-2]
    seq2[i] = seq2[i-1] + seq2[i-2]

res = 0
for i in range(n):
    res += seq1[i]/seq2[i]

print('%.4f' % res)