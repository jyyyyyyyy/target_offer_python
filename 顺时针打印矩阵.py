# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        array = []
        if matrix == None:
            return
        if matrix ==[]:
            return []
        start = 0
        row = len(matrix)#行数
        col = len(matrix[0])#列数
        while row > 2*start and col > 2*start:
            endX = col - 1 - start
            endY = row - 1 - start
            for i in range(start, endX+1):
                number = matrix[start][i]
                array.append(number)
            if start < endY:
                for i in range(start+1,endY+1):
                    number = matrix[i][endX]
                    array.append(number)
            if start < endX and start < endY:
                for i in range(endX-1,start-1,-1):
                    number = matrix[endY][i]
                    array.append(number)
            if start<endX and start<endY-1:
                for i in range(endY-1,start,-1):
                    number = matrix[i][start]
                    array.append(number)
            start += 1
        return array