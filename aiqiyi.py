def FindGreatestSumOfSubArray(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    max = array[0]
    sum = array[0]
    for i in range(1, len(array)):
        if sum < 0:
            sum = array[i]
        else:
            sum += array[i]
        if sum > max:
            max = sum
    return max

if __name__ == "__main__":
    array = list(input().split(','))
    array[0] = array[0][1:]
    array[-1]= array[-1][:-1]
    res = [int(i) for i in array]
    ans = FindGreatestSumOfSubArray(res)
    print(ans)


