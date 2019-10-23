import sys
n = int(sys.stdin.readline().strip())
values = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        values.append([int(lines[0]),int(lines[1])])
except:
    pass
def helper(n, values):
    def dfs(i, vals, flag):
        if flag[i] == -1:
            return True
        if flag[i] == 1:
            return False
        flag[i] = 1
        for j in vals[i]:
            if not dfs(j, vals, flag):
                return False
        flag[i] = -1
        return True
    val = [[] for _ in range(n)]
    flag = [0 for _ in range(n)]
    for cur, pre in values:
        val[pre].append(cur)
    for i in range(n):
        if not dfs(i, val, flag): return False
    return True
res = helper(n,values)
res = bool(1-res)
print(res)