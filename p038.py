def self_pandigital_check(string):
    for i in range(len(string)):
        for j in range(i,len(string)):
            if (i!=j) & (string[i] == string[j]):
                return True
    return False

num = 1
max = 0
max_num = 0
while True:
    if self_pandigital_check(str(num)):pass
    else:
        string = str(num)
        for i in range(2,10):
            string += str(num*i)
            if ((self_pandigital_check(string)) | ('0' in string)):break
            elif len(string)==9:
                print(num, string)
                if max<int(string):
                    max=int(string)
                    max_num=num
    num += 1
    if num>10000: break
print('')
print(max_num, max)

