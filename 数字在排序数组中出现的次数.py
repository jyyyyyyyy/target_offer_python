# 统计一个数字在排序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        if self.GetFirstOFK(data, k) == -1 or self.GetLastOFK(data, k)==-1:
            return 0
        return self.GetLastOFK(data, k) - self.GetFirstOFK(data, k) + 1

    def GetFirstOFK(self, data, k):
        low = 0
        high = len(data)-1
        while low <= high:
            mid = (low + high)//2
            if data[mid] < k:
                low = mid+1
            elif data[mid] > k:
                high = mid -1
            else:
                if mid == low or data[mid-1]!=k:
                    return mid
                else:
                    high = mid -1
        return -1
    def GetLastOFK(self, data, k):
        low = 0
        high = len(data)-1
        while low <= high:
            mid = (low+high)//2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == high or data[mid+1]!=k:
                    return mid
                else:
                    low = mid + 1
        return -1