sum=0
for i in range(1000):
    num = i+1
    power = 1
    for j in range(num):
        power = power * num
        power = power % 10000000000
    sum += power
    sum %= 10000000000
print(sum)