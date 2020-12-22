from math import gcd

# 1. 배열 생성부터 시작.
def listgenerator(num):
    result = [2]
    for i in range(0, int(num/3)+1):
        result+=[1,(i+1)*2,1]
    return result[:num]

# 2. 분수와 factor을 더하고 역수를 취하는 함수. 분수는 [분자, 분모] 리스트.
def onecalculator(fraction, num):
    result = [fraction[1]+fraction[0]*num, fraction[0]]
    return [result[0], result[1]]

# 3. n을 입력받으면 n번째의 분자와 분모를 반환하는 함수.
def fractioncalculator(num):
    if num==1: return [2,1]
    eulerlist = listgenerator(num)
    eulerlist.reverse()
    fraction = [eulerlist[0],1]
    for num in eulerlist[1:]:
        fraction = onecalculator(fraction, num)
    return fraction

for i in range(10):print(fractioncalculator(i+1))
print(sum(list(map(int,list(str(fractioncalculator(100)[0]))))))