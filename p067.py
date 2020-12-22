with open("p067_triangle.txt", "r") as text:
    num_list = []
    while True:
        line = text.readline()
        if not line: break
        num_list.append(line.split())
    for i in range(len(num_list)):
        for j in range(i+1):
            num_list[i][j] = int(num_list[i][j])
    for i in range(len(num_list)-1):
        for j in range(len(num_list[-2])):
            num_list[-2][j] += max(num_list[-1][j], num_list[-1][j+1])
        del num_list[-1]
    print(num_list)