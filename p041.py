from basicFunctions import PrimeDetector
from basicFunctions import PandigitalCheck

for i in range(7652410,1000000000):
    if i%100000==0: print('working on... :',i)
    if (PandigitalCheck(str(i)) & PrimeDetector(i)): print('pandigital prime:',i)

# ans: 7652413