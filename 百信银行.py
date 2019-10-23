N = int(input())
array = []
for i in range(1,N+1):
    if i < 10:
        array.append(i+i)
    else:
        sum = 0
        for num in str(i):
            sum += int(num)
        array.append(i+sum)

res = 0
for i in range(len(array)):
    if array[i] > N:
        res +=1

print(res)

