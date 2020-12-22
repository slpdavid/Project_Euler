def binaryConverter(num):
    factor=1
    while factor*2<=num:
        factor*=2
    result=0
    while factor>0:
        result*=10
        result+=int(num/factor)
        num%=factor
        factor=int(factor/2)
    return result

def palindromeGeneratorEven(num):
    string = str(num)
    string += string[::-1]
    return int(string)

def palindromeGeneratorOdd(num):
    string = str(num)
    string = string[:-1] + string[::-1]
    return int(string)

def isThisPalindrome(num):
    string = str(num)
    if string == string[::-1]:
        return True
    else:
        return False

sum=0
# EvenPalindrome
for i in range(1,1000):
    base10 = palindromeGeneratorEven(i)
    base2 = binaryConverter(base10)
    if isThisPalindrome(base2):
        sum+=base10
        print(base10,',',base2)

# OddPalindrome
for i in range(1,1000):
    base10 = palindromeGeneratorOdd(i)
    base2 = binaryConverter(base10)
    if isThisPalindrome(base2):
        sum += base10
        print(base10, ',', base2)

print(sum)