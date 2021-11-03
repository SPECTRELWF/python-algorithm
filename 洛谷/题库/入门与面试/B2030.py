import math

a, b = map(float, input().strip().split(" "))
c, d = map(float, input().strip().split(" "))

res = math.sqrt(((a - c) ** 2) + ((b - d) ** 2))
print("%.3f " % res)
