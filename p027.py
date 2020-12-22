def PrimeListGenerator(num):
    primeList = []
    basicPrimeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if num<100:
        for i in basicPrimeList:
            if i<=num: primeList.append(i)
        return primeList

    limit = int(num**0.5)
    primeList = PrimeListGenerator(limit)
    basicPrimeList = primeList.copy()

    for i in range(limit, num+1):
        check=True
        for j in basicPrimeList:
            if i%j==0:
                check=False
        if check: primeList.append(i)
    return primeList

def PrimeDetector(num):
    if num<2: return False
    primeList = PrimeListGenerator(num)
    if num == primeList[-1]:return True
    else: return False

max=0
for a in range(-1000, 1001):
    print(a)
    for b in range(-1000, 1001):
        n=0
        while True:
            value = n*n+a*n+b
            if PrimeDetector(value):pass
            else:break
            n+=1
        if max<n:
            max=n
            print('max length updated:',max,a,b)

# a=-59, b=231