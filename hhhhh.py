def printMatrix(matrix):
    #print(array)
    array = []
    if matrix == None:
        return
    if matrix == []:
        return []
    start = 0
    row = len(matrix)  # 行数
    col = len(matrix[0])  # 列数
    while row > 2 * start and col > 2 * start:
        endX = col - 1 - start
        endY = row - 1 - start
        for i in range(start, endX + 1):
            number = matrix[start][i]
            array.append(number)
        if start < endY:
            for i in range(start + 1, endY + 1):
                number = matrix[i][endX]
                array.append(number)
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                number = matrix[endY][i]
                array.append(number)
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start, -1):
                number = matrix[i][start]
                array.append(number)
        start += 1
    return array

if __name__ == "__main__":
    # line = list(map(int,input().split(' ')))
    # M = line[0]
    # N = line[1]
    # nums = []
    # for i in range(M):
    #     res = list(map(int, input().split(' ')))
    #     nums.append(res)
    # #print(array)
    # data = printMatrix(nums)
    # print(' '.join(str(i) for i in data))
    n = int(input())
    data = []
    for i in range(n):
        res = list(map(float,input().split(' ')))
        data.append(res)
    print(data)


float solu1(const vector<vector<float>> &data)
{
    int n = data.size();
    vector<vector<float>> dp(n+1, vector<float>(2, 0));
    for (int i = 1; i < n + 1; ++i)
    {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + data[i - 1][0];
        if(i >= 2)
            dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + data[i - 1][1];
    }
    return max(dp.back()[0], dp.back()[1]);
}
int main()
{
    int n = 0;
    cin >> n;
    vector<vector<float>> data(n, vector<float>(2, 0));
    for (int i = 0; i < n; ++i)
    {
        cin >> data[i][0];
        cin >> data[i][1];
    }
    cout << solu1(data);

    return 0;
}



