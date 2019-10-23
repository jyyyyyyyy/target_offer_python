m = int(input())
n = int(input())
array = []
for i in range(m):
    inputs = list(map(int, input().split(' ')))
    array.append(inputs)
row = 0
col = 0
sum = 0
if n == 1:
    for i in range(m):
        sum += array[i][0]
        print(array[i][0])
if m == 1:
    for i in range(n):
        sum += array[0][i]
if n > 1 and m > 1:
    while row < m and col < n:
        sum += array[row][col]
        if row + 1 >= m:
            col += 1
        elif col + 1>=n:
            row += 1
        elif array[row][col+1]<array[row+1][col]:
            col +=1
        else:
            row += 1
print(sum)

