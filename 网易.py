# import math
# def merge(tuple_before,tuple_after,array):
#     array_before = tuple_before[0]
#     cnt_before = tuple_before[1]
#     array_after = tuple_after[0]
#     cnt_after = tuple_after[1]
#     cnt = cnt_before+cnt_after
#     flag = len(array_after)-1
#     array_merge = []
#     nums = 0
#     for i in range(len(array_before)-1,-1,-1):
#         while array_before[i]<=array_after[flag] and flag>=0 :
#             array_merge.append(array_after[flag])
#             flag -= 1
#         if flag == -1 :
#             break
#         else:
#             array_merge.append(array_before[i])
#             nums += array.index(array_after[flag])-array.index(array_before[i])
#             cnt += (flag+1)
#     if flag == -1 :
#         for j in range(i,-1,-1):
#             array_merge.append(array_before[j])
#     else:
#         for j in range(flag ,-1,-1):
#             array_merge.append(array_after[j])
#     return array_merge[::-1],cnt,nums
#
# def mergesort(array):
#     if len(array)==1:
#         return (array,0)
#     cut = math.floor(len(array)/2)
#     tuple_before=mergesort(array[:cut])
#     tuple_after=mergesort(array[cut:])
#     return merge(tuple_before, tuple_after,array)
#
# if __name__ == "__main__":
#     num = int(input())
#     array = list(map(int, input().split(' ')))
#     print(mergesort(array)[2])

n = int(input())
num = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i + 1, n):
        if num[i] > num[j]:
            res = abs(i - j)
            sum += res
print(sum)