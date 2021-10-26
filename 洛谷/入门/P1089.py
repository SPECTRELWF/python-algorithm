res = 0
cnt = 0
for i in range(12):
    x = int(input(""))
    res += (300 - x)
    if res < 0:
        print(-(i+1))
        break;
    else:
        cnt += int(res/100)
        res %= 100
if res >= 0:
    print(int(cnt*120)+res)