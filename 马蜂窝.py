line1 = input()
line2 = input()
str1 = line1[1:-1]
prefer_tags = list(map(str,str1.split(',')))
for i in range(len(prefer_tags)):
    prefer_tags[i]=prefer_tags[i][1:-1]
#print(prefer_tags)
str2 = line2[2:-2]
candidates = str2.split('],[')
for i in range(len(candidates)):
    temp = candidates[i].split(',')
    #print(temp)
    array = []
    for s in temp:
        s = s[1:-1]
        array.append(s)
    candidates[i]=array

res = []
for i in range(len(candidates)):
    for j in range(i+1,len(candidates)):
        if candidates[i]+candidates[j] == prefer_tags:
            res.append(i)
            res.append(j)
res = [str(i) for i in res]
print(','.join(res))