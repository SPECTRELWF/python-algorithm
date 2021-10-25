"""
P1035 [NOIP2002 普及组] 级数求和
题目描述
已知：S_n= 1+\frac{1}{2}+\frac{1}{3}+…+\frac{1}{n}S 
n
​	
 =1+ 
2
1
​	
 + 
3
1
​	
 +…+ 
n
1
​	
 。显然对于任意一个整数 kk，当 nn 足够大的时候，S_n>kS 
n
​	
 >k。

现给出一个整数 kk，要求计算出一个最小的 nn，使得 S_n>kS 
n
​	
 >k。

输入格式
一个正整数 kk。

输出格式
一个正整数 nn。

"""

k = int(input())
res = 0
for i in range(100000000):
    res += 1.0 / (i+1)
    if res > k:
        print(i+1)
        break