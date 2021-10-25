"""
P1014 [NOIP1999 普及组] Cantor 表
题目描述
现代数学的著名证明之一是 Georg Cantor 证明了有理数是可枚举的。他是用下面这一张表来证明这一命题的：

1/11/1 , 1/21/2 , 1/31/3 , 1/41/4, 1/51/5, …

2/12/1, 2/22/2 , 2/32/3, 2/42/4, …

3/13/1 , 3/23/2, 3/33/3, …

4/14/1, 4/24/2, …

5/15/1, …

…

我们以 Z 字形给上表的每一项编号。第一项是 1/11/1，然后是 1/21/2，2/12/1，3/13/1，2/22/2，…

输入格式
整数NN（1 \leq N \leq 10^71≤N≤10 
7
 ）。

输出格式
表中的第 NN 项。


"""

def s(k):
    return k*(k+1)/2
 
myinput=int(input())
k=1
while(True):
    if s(k) >=myinput:
        break
    k+=1
index=myinput-s(k-1)#第k条线的正数第index个元素  
if k%2==0:    
    print("%d/%d"%(index,k-index+1))
elif k%2==1:
    print("%d/%d"%(k-index+1,index))
 