f = open("p022_names.txt", 'r')
line = f.readline()
line = line.replace('"', '')
name_list = line.split(",")
name_list.sort()
print(name_list[0:5], '...')
final_score = 0
for i in range(len(name_list)):
    score_sum = 0
    for char in name_list[i]:
        score_sum = score_sum + ord(char) - 64
    final_score = final_score + score_sum * (i+1)
    if i==937:
        print(name_list[i], score_sum*(i+1))
print(final_score)
f.close()