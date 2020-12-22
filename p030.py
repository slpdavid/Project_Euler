sum=0
for a6 in range(0,10):
    for a5 in range(0,10):
        for a4 in range(10):
            for a3 in range(10):
                for a2 in range(10):
                    for a1 in range(10):
                        num1 = a6*100000+a5*10000+a4*1000+a3*100+a2*10+a1
                        num2 = a6**5+a5**5+a4**5+a3**5+a2**5+a1**5
                        if num1==num2:
                            print(num1)
                            sum+=num1
print(sum)