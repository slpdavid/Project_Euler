def CoinSum(num, coinlist2, count):
    coinlist = coinlist2.copy()
    if num==0:
        return count+1
    while coinlist[-1] > num:
        del coinlist[-1]
    currentcoin = coinlist[-1]
    del coinlist[-1]
    coin_num = int(num / currentcoin)
    if coinlist==[]:
        return count+1
    while coin_num >= 0:
        count = CoinSum(num - currentcoin * coin_num, coinlist, count)
        coin_num -= 1
    return count

num = 200
coinlist = [1,2,5,10,20,50,100, 200]
count = 0
print(CoinSum(num, coinlist, count))