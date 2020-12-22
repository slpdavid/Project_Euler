from basicFunctions import PrimeDetector

i=1
while True:
    num=2*i+1
    if PrimeDetector(num):
        pass
    else:
        j=1
        square=2*j*j
        while num>square:
            if PrimeDetector(num-square):
                break
            else:
                j+=1
                square=2*j*j
        if square>num:
            break
    i+=1
print(num)