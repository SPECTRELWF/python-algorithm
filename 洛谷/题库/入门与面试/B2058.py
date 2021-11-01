'''
Author: your name
Date: 2021-10-31 20:48:44
LastEditTime: 2021-10-31 23:52:47
LastEditors: your name
Description: In User Settings Edit
FilePath: \python刷算法题\入门与面试题库\B2058.py
'''
n = int(input())
x,y,z = 0,0,0
for i in range(n):
    a , b , c = map(int,input().split(" "))
    x += a
    y += b
    z += c
    
print(x,y,z,x+y+z)
    