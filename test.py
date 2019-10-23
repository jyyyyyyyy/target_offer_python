import sys

#line1= sys.stdin.readline().strip()
line2= sys.stdin.readline().strip()
# line1 = int(line1)
nums = list(map(int, line2.split(' ')))

m = max(nums)

num_dict = {}
for n in nums:
    if n not in num_dict:
        num_dict[n] = 1
    else:
        num_dict[n] += 1
res = 0
for i in range(1, m+1):
    prob1 = 1
    prob2 = 1
    for k in num_dict:
        if k >= i:
            prob2 *= ((i-1)/float(k))**num_dict[k]
            prob1 *= (i/float(k))**num_dict[k]
    prob = prob1 - prob2
    # print('r', i, prob)
    res += i * prob
print(res)