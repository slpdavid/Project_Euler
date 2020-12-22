def GetPrimeList():
    primeList = []
    f = open('PrimeBelowMillion.txt')
    while True:
        line = f.readline()
        if not line: break
        primeList.append(int(line))
    f.close()
    return primeList

primeList = GetPrimeList()

def LargePrimeListGenerator(num):
    for i in range(1000000, num+1):
        limit = int(i**0.5)
        check=True
        for j in primeList:
            if j>limit: break
            elif i%j==0:
                check=False
                break
        if check:
            primeList.append(i)
    return primeList

def PrimeDetector(num):
    limit = num ** 0.5
    for i in primeList:
        if i>limit: return True
        elif num%i==0: return False
    return True

def PandigitalCheck(string):
    # 1. check 0
    if '0' in string: return False

    # 2. check number overflow
    digit = len(string)
    num_list = list(range(1, digit + 1))
    for i in string:
        if not (int(i) in num_list): return False

    # 3. check overlapped number
    for i in range(len(string)):
        for j in range(i,len(string)):
            if (i!=j) & (string[i] == string[j]):
                return False
    return True