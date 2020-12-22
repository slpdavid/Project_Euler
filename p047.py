from basicFunctions import GetPrimeList
from basicFunctions import PrimeDetector

primeList = GetPrimeList()

def FactorCalculator(num):
    factorNumber=0
    for i in primeList:
        if i>num: break
        if num%i == 0:
            factorNumber += 1
    return factorNumber

i=2
count=0
while True:
    if i%10000==0: print(i)
    if FactorCalculator(i)==4:
        count+=1
        if count==4:
            print(i-3, i-2, i-1, i)
            break
    else:
        count=0
    i+=1
