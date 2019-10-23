# inputs = input().split()
# N = int(inputs[0])
# M = int(inputs[1])
# car = input()
# man = input()
# count = 0
# s = man
# all = [s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x)]
# #print(all)
# all_car = []
# for i in range(N):
#     temp = car[i:]+car[:i]
#     all_car.append(temp)
# for i in all:
#     for j in all_car:
#         if i in j:
#             count+=1
#             break
# print(count)

inputs = input().split()
n = int(inputs[0])
q = int(inputs[1])
for i in range(q):
    input().split()