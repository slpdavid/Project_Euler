f = open('PrimeBelowMillion.txt')
primeList = []
while True:
    line = f.readline()
    if not line: break
    primeList.append(int(line))
f.close()

new_primeList = [2]
for prime in primeList:
    str_prime = str(prime)
    if prime==23: new_primeList.append(prime)
    elif ('2' in str_prime) | ('4' in str_prime) | ('6' in str_prime) | ('8' in str_prime) | ('0' in str_prime): pass
    else: new_primeList.append(prime)

print(new_primeList)

truncatablePrime = []

def TruncatableDetector(prime):
    if not (prime in new_primeList): return False
    prime_string = str(prime)
    # print(prime_string)
    while len(prime_string) > 1:
        prime_string = prime_string[1:]
        if not (int(prime_string) in new_primeList): return False
        # print(prime_string)
    prime_string = str(prime)
    while len(prime_string) > 1:
        prime_string = prime_string[:-1]
        if not (int(prime_string) in new_primeList): return False
        # print(prime_string)
    return True

sum = 0
for prime in new_primeList[4:]:
    if TruncatableDetector(prime):
        print(prime)
        sum += prime
print('')
print(sum)