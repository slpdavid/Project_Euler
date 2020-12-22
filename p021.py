import numpy as np

def DivisorList(num):
    limit = int(np.sqrt(num))
    divisor_list = []
    for i in range(limit):
        if num % (i+1) == 0:
            divisor_list.append(i+1)
            if (int(num/(i+1)) != (i+1)) & (i != 0):
                divisor_list.append(int(num/(i+1)))
    return divisor_list

'''
result_list = []
for i in range(2, 10000):
    temp = sum(DivisorList(i))
    if (temp != i) & (temp != 1) & (temp < 10000):
        temp2 = sum(DivisorList(temp))
        if temp2 == i:
            print(i, 'and', temp,'are amicable numbers.')
            print('d(', i, '):', temp)
            print('d(', temp, '):', temp2)
            print('')
            result_list.append(i)
print(result_list)
print(sum(result_list))
'''