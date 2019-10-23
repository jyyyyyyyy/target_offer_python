def qick_sort(nums,begin,end):
    left = begin
    right = end
    tmp = nums[begin]
    while left != right:
        while left<right and nums[right]>tmp:
            right -= 1
        while left < right and nums[left]<tmp:
            left += 1
        if left<right:
            nums[left],nums[right] = nums[right],nums[left]
    tmp,nums[left]=nums[left],tmp
    if left-begin>1:
        qick_sort(nums,begin,left-1)
    if end-right>1:
        qick_sort(nums,right+1,end)
    return nums
if __name__ == "__main__":
    nums = [4,5,1,6,2,7,3,8]
    res = qick_sort(nums,0,len(nums)-1)
    print(res)