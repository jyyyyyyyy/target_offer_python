line = list(map(int,input().split()))
tree = line[0]
people = line[1]
array=[]
for i in range(people):
    array.append(list(map(int,input().split())))
num = 0
sum = []
num = array[0][1]-array[0][0]+1
sum.append(num)
for i in range(1,people):
    if array[i][0] == array[i-1][1]:
        tag = array[i][1]-array[i][0]
        num += tag
        sum.append(num)
    else:
        tag = array[i][1]-array[i][0]+1
        num += tag
        sum.append(num)
for i in sum:
    print(i)
#
# line = list(map(int,input().split()))
# n = line[0]
# m = line[1]
# array = list(map(int,input().split()))
# array.sort()
# res = 0
# i = 0
# j = 2*m-1
# while i < j:
#     res += array[i]*array[j]
#     i+=1
#     j-=1
# print(res)

line = list(map(int,input().split()))
n = line[0]
m = line[1]
dp = [0]*100000
count = 0
ans = []
for i in range(m):
    temp =input().split(' ')
    left = int(temp[0])
    right = int(temp[1])
    res = 0
    for j in range(left,right+1):
        if dp[j] == 0:
            dp[j] =1
            res+=1
    count += res
    ans.append(count)
for i in ans:
    print(i)
#
#
#
#
#
# line = list(map(int,input().split()))
# n = line[0]
# m = line[1]
# dp = dict()
# count = 0
# ans = []
# for i in range(m):
#     temp =input().split(' ')
#     left = int(temp[0])
#     right = int(temp[1])
#     res = 0
#     for j in range(left,right+1):
#         if j not in dp.keys():
#             dp[j] =1
#             res+=1
#     count += res
#     ans.append(count)
# for i in ans:
#     print(i)
