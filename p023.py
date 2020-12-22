import numpy
import p021

limit = 28124
abundant_list = []
for i in range(2, limit):
    if i < sum(p021.DivisorList(i)):
        abundant_list.append(i)
print('abundant list creation complete')

non_abundant_sum_list = list(range(1,limit))
for i in range(1, limit):
    if i%1000==0:
        print('Current number:', i)
    j = 0
    while (abundant_list[j] * 2) <= i:
        pair = i - abundant_list[j]
        if pair in abundant_list:
            # print(i, '=', abundant_list[j], '+', pair)
            non_abundant_sum_list.remove(i)
            break
        j = j + 1

# print('abundant list:', abundant_list)
# print('non abundant sum list: ', non_abundant_sum_list)
print('answer:', sum(non_abundant_sum_list))