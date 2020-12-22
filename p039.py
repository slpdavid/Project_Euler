triangle_list = [0]*1000
for a in range(1,500):
    for b in range(a,501-a):
        for c in range(b, 1001-a-b):
            if a*a+b*b==c*c:
                print(a,b,c)
                print(a+b+c, 'updated')
                triangle_list[a+b+c-1] += 1
max=0
max_idx=0
for i in range(1000):
    if max<triangle_list[i]:
        max=triangle_list[i]
        max_idx=i+1
print(max_idx,max)