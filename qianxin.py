#
# num= input()
# numlist1 = []
# numlist2 = []
# for char in num:
#     try:
#         int(char)
#         numlist1 += char
#     except:
#         if len(numlist2) > len(numlist1):
#             pass
#         else:
#             numlist2 = numlist1
#             numlist1 = []
#     # 结果输出
# result = ''.join(numlist2)
# res = str(len(result))+'/'+result
# # print("%s,%d" % (result, length))
# print(res)

# coding=utf-8
num = input()

for line in num:
    # 字符串转列表进行遍历
    str = list(line)
    count = 0
    length = 0
    temp = []
    dig = []
    for i in range(str.__len__()):
        if (str[i] >= '0' and str[i] <= '9'):
            # 数字加一
            count += 1
            temp.append(str[i])
        else:
            if count >= length:
                # 数字串大于之前的，由于题目要求长度相等输出最后一串，所以这里要用大于等于
                length = count
                count = 0
                dig = temp.copy()
                temp = []
            else:
                # 数字串较短则清空
                temp = []
                count = 0
    # 结果输出
result = ''.join(dig)
print("%s,%d" % (result, length))

