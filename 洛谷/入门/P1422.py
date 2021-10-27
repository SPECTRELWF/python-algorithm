n = int(input())
res = 0
if n <= 150:
    res = n*0.4463
elif n > 150 and n < 401:
    res = 150*0.4463 + (n-150)*0.4663
else:
    res = 150*0.4463 + 250*0.4663 + (n-400)*0.5663
print('%.1f'%res)