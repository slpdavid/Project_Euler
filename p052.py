i=1
factor=10
while True:
    if 6*i>factor:
        i=factor
        factor*=10
    str1 = sorted(str(i))
    str2 = sorted(str(2*i))
    str3 = sorted(str(3 * i))
    str4 = sorted(str(4 * i))
    str5 = sorted(str(5 * i))
    str6 = sorted(str(6 * i))
    if (str1==str2)&(str2==str3)&(str3==str4)&(str4==str5)&(str5==str6):
        print(i)
    i+=1
    if i>10000000: break