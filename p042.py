triangleList = []
num=0
for i in range(1,101):
    num+=i
    triangleList.append(num)

f = open('p042_words.txt','r')
line = f.read()
line = line.replace('"','')
line = line.split(',')
f.close()

result = 0
for word in line:
    sum = 0
    for i in word:
        sum += ord(i)-64
    if sum in triangleList:
        print(word)
        result+=1

print(result)