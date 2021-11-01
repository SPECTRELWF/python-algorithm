'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-11-01 00:18:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2068.py
'''
n = int(input())
data = input().strip().split(' ')
res = 0
for i in data:
    if int(i[3]) > int(i[0])+int(i[1])+int(i[2]):
        res += 1
    
print(res)