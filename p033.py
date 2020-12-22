result_list=[]
for samedigit in range(10):
    for firstdigit in range(10):
        for seconddigit in range(10):
            # s1/2s
            num1 = int(str(samedigit) + str(firstdigit))
            num2 = int(str(seconddigit) + str(samedigit))
            # 1/2
            num3 = firstdigit
            num4 = seconddigit
            # print(num1,'/',num2,',',num3,'/',num4)
            if (num2 == 0) | (num4 == 0):
                pass
            elif (num1 < 10) | (num2 < 10):
                pass
            elif (num1 == num2):
                pass
            else:
                if num1 / num2 == num3 / num4:
                    print(num1, '/', num2, ',', num3, '/', num4)
                    result_list.append([num1, num2])