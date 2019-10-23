
# n = int(input())
# res = [0]*n
# if n <= 2:
#     for i in range(n):
#         res[i] = 3
# if n>2:
#     res[0]=3
#     res[1]=3
#     for j in range(2,n):
#         res[j]=res[j-1]+res[j-2]
# temp = 0
# for k in range(n-1,-1,-1):
#     temp = (temp+res[k])*2
# print(temp)
line = list(input().split(';'))
#print(line)
new = []
for s in line:
    if s != '':
        new.append(s)
news=[]
for i in new:
    if i.isalpha():
        news.append(i)
res = [0]*len(news)
for i in range(len(news)):
    res[i] = abs(ord(news[i][0])-ord(news[i][-1]))
print(sum(res))
