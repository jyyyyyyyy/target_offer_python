import sys

def main():

    line = sys.stdin.readline().strip()
    values = list(map(int,line.split(' ')))
    n = values[0]
    m = values[1]
    k = values[2]
    array = []
    for i in range(n):
        for j in range(m):
            array.append((i+1)*(j+1))
    #print(array)

    num= findkth(array, 0, len(array) - 1, k)
    print(num)


def quicksort(num, low, high):  # 快速排序
    if low < high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)


def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] > pivot):
            high -= 1
        while (low < high and num[low] < pivot):
            low += 1
        temp = num[low]
        num[low] = num[high]
        num[high] = temp
    num[low] = pivot
    return low


def findkth(num, low, high, k):  # 找到数组里第k个数
    index = partition(num, low, high)
    if index == k: return num[index]
    if index < k:
        return findkth(num, index + 1, high, k)
    else:
        return findkth(num, low, index - 1, k)


if __name__ == '__main__':
    main()