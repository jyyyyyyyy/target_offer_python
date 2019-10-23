# n = int(input())
# res = [[]] * (n+1)
# ans = []
# for row in range(len(res)):
#     res[row] = [None]*(row+1)
#     for col in range(len(res[row])):
#         if col == 0 or col == row:
#             res[row][col]=1
#         else:
#             res[row][col] = res[row-1][col]+res[row-1][col-1]
# ans = [str(i) for i in res[len(res)-1]]
# print(' '.join(ans))

class Node():
    def __init__(self,item):
        self.item=item
        self.isin=False
        self.left=None
        self.right=None
def HuffmanTree(l,re):
    temp = []
    for x in range(0, len(l)):
        temp.append(Node(l[x]))
    K = Node(float('inf'))
    while len(temp) < 2 * len(l) - 1:
        m1 = m2 = K
        for x in range(len(temp)):
            if m1.item > temp[x].item and (temp[x].isin is False):
                m2 = m1
                m1 = temp[x]
            elif m2.item > temp[x].item and (temp[x].isin is False):
                m2 = temp[x]

        H = Node(m1.item + m2.item)
        H.right = m1
        H.left = m2
        temp.append(H)
        m1.isin = m2.isin = True
        re.append(H.item)
    return re[-1]
if __name__=='__main__':
    n = int(input())
    an = list(map(int, input().split()))
    an.sort()
    if n<=2:
        print(max(an))
    else:
        re = []
        res=HuffmanTree(an,re)
        print(res)

