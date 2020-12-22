def get_next_permutation(string):
    i = len(string) - 2
    while i >= 0:
        if string[i] < string[i + 1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i]) + 1)
            last_nums = ''.join(target)
            return string[:i] + new_num + last_nums
        i -= 1

def StrangeFunction(string):
    if not (int(string[1:4]) % 2 == 0): return False
    if not (int(string[2:5]) % 3 == 0): return False
    if not (int(string[3:6]) % 5 == 0): return False
    if not (int(string[4:7]) % 7 == 0): return False
    if not (int(string[5:8]) % 11 == 0): return False
    if not (int(string[6:9]) % 13 == 0): return False
    if not (int(string[7:10]) % 17 == 0): return False
    return True

string = '1023456789'
sum=0
while True:
    string = get_next_permutation(string)
    if StrangeFunction(string):
        print(string)
        sum+=int(string)
    if string=='9876543210': break

print(string+'stop')
print(sum)