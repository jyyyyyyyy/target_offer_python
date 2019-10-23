
line = list(map(int,input().split(' ')))
n = line[0]
k = line[1]
array = []
nums = []
hard = []
for i in range(n):
    array = list(map(int,input().split(' ')))
    nums.append(array[0])
    hard.append(array[1])
ans = 0
if n == k:
    for i in range(n):
        ans += nums[i]
    small = hard[0]
    for i in range(n):
        if hard[i]<small:
            small = hard[i]
    res = ans * small
    print(res)
else:
    res = []
    list2 = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i != j:
                list2.append((nums[i], nums[j]))

    #comb = [list(i) for i in itertools.combinations(nums, k)]
    for i in list2:
        ans = sum(i)
        hards = []
        for j in range(k):
            indx = nums.index(i[j])
            hards.append(hard[indx])
        small = min(hards)
        res.append(ans*small)
    print(max(res))


n = int(input())
str_all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    K = int(input())
    line = input()
    value = list(map(str, line.split()))
    value1 = value[0]
    value2 = value[1]
    def ten_2K(num):
        res = ""
        while num>0:
            res = str_all[num%K]+res
            num//=K
        return res
    def K2_ten(res):
        len_res = len(res)
        num = 0
        for i in range(len_res):
            num = str_all.find(res[i])*pow(K,len_res-i-1)+num
        return num
    value1_trans = K2_ten(value1)
    value2_trans = K2_ten(value2)
    if value[2] == '-':
        fin_res = value1_trans-value2_trans
    elif value[2] == '+':
        fin_res = value1_trans + value2_trans
    else:
        fin_res = value1_trans * value2_trans
    print(ten_2K(fin_res))


