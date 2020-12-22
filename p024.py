digit_list = list(range(0, 10))

factorial_list = [1]

for i in range(9):
    factorial_list.append(factorial_list[-1]*(i+1))
del factorial_list[0]

print(factorial_list)

target = 1000000
result_list = []
index = 0
while True:
    digit = 0
    while target > factorial_list[-1]:
        target = target - factorial_list[-1]
        digit = digit + 1
    print(index+1,'digit is',digit_list[digit])
    result_list.append(digit_list[digit])
    digit_list.remove(digit_list[digit])
    del factorial_list[-1]
    index+=1
    if target==0:
        break
print(result_list)