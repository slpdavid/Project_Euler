def TGen(num):
    return int(num*(num+1)/2)

def PGen(num):
    return int(num*(3*num-1)/2)

def HGen(num):
    return int(num*(2*num-1))

TIdx, PIdx, HIdx = 1, 1, 1
TNum, PNum, HNum = 1, 1, 1

while True:
    minimum = min(TNum, PNum, HNum)
    if minimum == TNum:
        TIdx += 1
        TNum = TGen(TIdx)
    if minimum == PNum:
        PIdx += 1
        PNum = PGen(PIdx)
    if minimum == HNum:
        HIdx += 1
        HNum = HGen(HIdx)
    if (TNum == PNum) & (TNum == HNum):
        print(TNum, TIdx, PIdx, HIdx)