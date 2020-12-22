import numpy as np

# print(num_list.shape)

def counter(num):
    num_list = np.zeros(num*100)
    for i in range(1,100):
        num_list[(i+1)*num-1]=1

    for i in range(num-1):
        for j in range(1,100):
            num_list[(i+1)*(j+1)-1] = 0
    count = 0
    for i in num_list:
        if i:count+=1
    return count

print(counter(1))
print(counter(2))
print(counter(3))
print(counter(4))
print(counter(5))
print(counter(6))


