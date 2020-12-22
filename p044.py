def PentagonGenerator(num):
    return int(num*(3*num-1)/2)

def NumDiffGen(num):
    return PentagonGenerator(num)-PentagonGenerator(0)

def SumDiffGen(curr_idx, idx_diff):
    return PentagonGenerator(curr_idx+idx_diff) + PentagonGenerator(curr_idx), PentagonGenerator(curr_idx+idx_diff) + PentagonGenerator(curr_idx)


# Pentagon numbers 리스트 갯수
list_idx = 10
# curr_diff 계산시 간격
idx_diff = 1
# 현재 idx
curr_idx = 0
# limit
num_diff = NumDiffGen(idx_diff+1)

pentagon_list = []
for i in range(list_idx):
    pentagon_list.append(PentagonGenerator(i))

while True:
    # 현재 D 계산
    curr_sum, curr_diff = Diffgen(curr_idx, idx_diff)
    # list 최대치와 비교하여 리스트 갱신
    while pentagon_list[-1] < curr_sum:
        list_idx += 1
        pentagon_list.append(PentagonGenerator(list_idx))
    # 합, 차가 list에 있는지 확인
    check = (curr_sum in pentagon_list) & (curr_diff in pentagon_list)

    if check:
        print(PentagonGenerator(curr_idx+idx_diff), ',', PentagonGenerator(curr_idx))
        break

    