n , m = map(int,input().split(" "))
s2 = ((m+1)*(n+1)*m*n)/4
nn = min(n,m)
s1 = m*n*(nn+1)+nn*(nn+1)*(2*nn+1)/6 - (m+n)*nn*(nn+1)/2
print(int(s1),int(s2-s1))