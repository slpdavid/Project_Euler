num = int(input())
sum = 1
add = 6
add_add = 13
for i in range(1, num+1):
    sum += add*4
    add += add_add
    add_add += 8
print(2*num+1, 'th sum:', sum)