PRIME_LIST = [3,7,11,13,17,19,23,29,31,37]
NUM_LIST = list(range(2,1000))

for i in NUM_LIST:
    if (i%2==0) | (i%5==0):
        check=True
        for j in PRIME_LIST:
            if (i>j) & (i%j==0):
                check=False
        if check:
            NUM_LIST.remove(i)

def GetCycle(num):
    while num%2==0:
        num/=2
    while num%5==0:
        num/=5
    num=int(num)
    digit=1
    while True:
        factor = 1
        for i in range(digit):
            factor = factor * 10
        factor -= 1
        if factor%num==0:
            return digit
        digit+=1
max_cycle = 0
d = 1
for i in NUM_LIST:
    cycle=GetCycle(i)
    if max_cycle<cycle:
        print('maximum updated. new d:',i)
        print('cycle length=',cycle)
        max_cycle=cycle
        d=i

print(d, GetCycle(d))