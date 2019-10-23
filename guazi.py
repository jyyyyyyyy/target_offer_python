# s = input()
# v, w, p = 0, int(s>''), ''
# for d in s:
#     v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
# print(w)

S = input()
K = int(input())
if K>1:
    print("".join(sorted(S)))
n = len(S)
minS= S
for i in range(n):
    S = S[1:]+S[0]
    if S<minS:
        minS = S
print(minS)