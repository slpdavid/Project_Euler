from basicFunctions import GetPrimeList

primeList = GetPrimeList()

num = 2
while True:
    idx = 0
    while True:
        sum = 0
        for i in range(num):
            sum += primeList[idx+i]
        if sum>1000000: break
        if sum in primeList:
            print(sum, num)
            break
        idx += 1
    num+=1
    if num>len(primeList): break
