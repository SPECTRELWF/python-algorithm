start, step, epoch = map(int, input().split(" "))

res = start + (step - start) * (epoch - 1)
print(res)
