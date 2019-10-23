from itertools import permutations


def bubble_sort(nums):
    number = 0
    for i in range(len(nums) - 1):
        ex_flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        number += 1
        if not ex_flag:
            return nums  # 这里代表计算机偷懒成功 (〃'▽'〃)

    return number  # 这里代表计算机没有偷懒成功 o(╥﹏╥)o
if __name__ == "__main__":
    line = list(input().split())
    n = int(line[0])
    r = int(line[1])
    array = []
    for i in range(1, n + 1):
        array.append(i)
    allarray = list(permutations(array, n))  # 排列
    print(allarray)
    sum = 0
    for num in allarray:
        num = list(num)
        number = bubble_sort(num)
        if(number == r):
            print(num)
            sum += 1
    print(sum%20150204)

