
line = input()
a = list(map(int, line.split(' ')))

left = 0
right = len(a)-1
small = 0
big = 0
while left < right:
    if a[left]>a[right]:
        small += a[left]
        left += 1
        if a[left] > a[right]:
            big += a[left]
            left += 1
        else:
            right -= 1
    if a[left]<a[right]:
        small += a[right]
        right -= 1
        if a[left] <= a[right]:
            big += a[right]
            right -= 1
        else:
            left += 1
    if a[left]==a[right]:
        if a[left+1] > a[right-1]:
            small += a[right]
            right -= 1
            if a[left] > a[right]:
                big += a[left]
                left += 1
            else:
                right -= 1
        else:
            small += a[left]
            left += 1
            if a[left] > a[right]:
                big += a[left]
                left += 1
            else:
                right -= 1

if small >= big:
    print('YES')
else:
    print('NO')

