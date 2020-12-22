f = open('PrimeBelowMillion.txt', 'r')
primeList = []
while True:
    line = f.readline()
    if not line: break
    primeList.append(int(line))
f.close()

new_primeList = [2]
for prime in primeList:
    str_prime = str(prime)
    if ('2' in str_prime) | ('4' in str_prime) | ('6' in str_prime) | ('8' in str_prime) | ('0' in str_prime): pass
    else: new_primeList.append(prime)

def CircularDetector(num):
    string_num = str(num)
    length = len(string_num)
    if length == 1: return True
    else:
        for i in range(length):
            string_num = string_num[1:]+string_num[0]
            if int(string_num) in new_primeList: pass
            else: return False
    return True

circular_prime_list=[]
for num in new_primeList:
    if CircularDetector(num): circular_prime_list.append(num)

print(circular_prime_list)
print(len(circular_prime_list))