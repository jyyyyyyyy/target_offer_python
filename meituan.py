n = int(input())

item = [int(x) for x in (input().split(' '))]
box = [int(x) for x in (input().split(' '))]

dic = {}
for i in range(len(box)):
    dic[box[i]] = item[i]

box = sorted(box, reverse=True)
all = sum(item)
k = 1
for i in range(len(box)):
    if all > box[i]:
        all -= box[i]
        k += 1
    else:
        break
t = 0
for j in range(k):
    t += box[j]-dic[box[j]]

print(k,t)
