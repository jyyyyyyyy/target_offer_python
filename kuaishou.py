# # -*- coding: cp936 -*-
# str1 = input()
# str2 = input()
#
# matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
#
# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#         if str1[i - 1] == str2[j - 1]:
#             d = 0
#         else:
#             d = 1
#         matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)
#
# print(matrix[len(str1)][len(str2)])

# def shudu(array):
#     raw = [{},{},{},{},{},{},{},{},{}]
#     col = [{},{},{},{},{},{},{},{},{}]
#     cell = [{},{},{},{},{},{},{},{},{}]
#     for i in range(9):
#         for j in range(9):
#             num = (3*(i//3)+j//3)
#             temp = array[i][j]
#             if temp !="X":
#                 if temp not in raw[i] and temp not in col[i] and temp not in cell[num]:
#                     raw[i][temp] = 1
#                     col[j][temp] = 1
#                     cell[num][temp] = 1
#                 else:
#                     return 'false'
#     return 'true'
#
# num = []
# for i in range(9):
#     s = input()
#     b = []
#     for j in s:
#         b.append(j)
#     num.append(b)
# a = shudu(num)
# print(a)

# def shudu(array):
#     raw = [{},{},{},{},{},{},{},{},{}]
#     col = [{},{},{},{},{},{},{},{},{}]
#     cell = [{},{},{},{},{},{},{},{},{}]
#     for i in range(9):
#         for j in range(9):
#             num = (3*(i//3)+j//3)
#             temp = array[i][j]
#             if temp !="X":
#                 if temp not in raw[i] and temp not in col[i] and temp not in cell[num]:
#                     raw[i][temp] = 1
#                     col[j][temp] = 1
#                     cell[num][temp] = 1
#                 else:
#                     return 'false'
#     return 'true'
#
# num = []
# for i in range(9):
#     words = list(input())
#     num.append(words)
# res = shudu(num)
# print(res)

num=int(input())
def get_num_factors(num):
    list0=[]
    tmp=2
    if num==tmp:
        return 1
    else:
        while (num>=tmp):
            k=num%tmp
            if(k == 0):
                list0.append(int(tmp))
                num=num/tmp #更新
            else:
                tmp=tmp+1 #同时更新除数值，不必每次都从头开始
    # print(' '.join(list0)+' ')
    # print(list0)
    return len(list0)

ans= []
# print(num)
for i in range(2,num+1):
    res = get_num_factors(i)
    # print(res)
    # res = sum(res)
    ans.append(res)
# print(ans)
print(sum(ans))

