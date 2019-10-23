# n = int(input())
# count = 0
# while n >0:
#     if n != 0:
#         n = n & (n-1)
#     count += 1
# print(count)


xs = list(map(int,input().split()))
k = int(input())
print(xs)
res = []
for i in range(len(xs)):
    if i+k<=len(xs):
        temp = format(sum(xs[i:i+k])/k,'.2f')
        res.append(temp)
res = [str(x) for x in res]
print(' '.join(res))