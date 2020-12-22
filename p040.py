def DigitFinder(num):
    digit=1
    factor=1
    while num>9*factor*digit:
        num-=9*factor*digit
        digit+=1
        factor*=10
    target=factor+int((num-1)/digit)
    print(str(target)[(num-1)%digit])
    return int(str(target)[(num-1)%digit])

result = DigitFinder(1)*DigitFinder(10)*DigitFinder(100)*DigitFinder(1000)*DigitFinder(10000)*DigitFinder(100000)*DigitFinder(1000000)
print(result)