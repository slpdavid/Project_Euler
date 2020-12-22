fac_list = [1,1,2,6,24,120,720,5040,40320,362880]

def factorial(num):
    return fac_list[num]

for i in range(10000000):
    num=i
    factor=10
    sum=0
    while num!=0:
        digit=num%factor
        sum+=factorial(digit)
        num=int(num/factor)
    if i==sum: print(i)