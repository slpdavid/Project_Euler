def self_pandigital_check(string):
    for i in range(len(string)):
        for j in range(i,len(string)):
            if (i!=j) & (string[i] == string[j]):
                return True
    return False

result_list = []
for a in range(1, 100):
    for b in range(100, 10000):
        while True:
            if (a<10)&(b<1000): break
            if (a>=10)&(b>=1000): break
            str_a = str(a)
            str_b = str(b)
            if '0' in str_b: break
            check = False
            check = self_pandigital_check(str_a)
            if check: break
            check = self_pandigital_check(str_b)
            if check: pass
            for digit_a in str_a:
                for digit_b in str_b:
                    if digit_a == digit_b:
                        check = True
                        break
            if check: break
            c = a*b
            if c>=10000: break
            if c<1000: break
            str_c = str(c)
            if '0' in str_c: break
            check = self_pandigital_check(str_c)
            if check: break

            for digit_a in str_a:
                for digit_b in str_b:
                    for digit_c in str_c:
                        if (digit_a == digit_c) | (digit_b == digit_c):
                            check = True
                            break
            if check: break
            for i in result_list:
                if i[2]==c: check=True
            if check: break
            result_list.append([a,b,c])
            break
for i in result_list: print(i)
sum=0
for i in result_list:
    sum += i[2]
print(sum)