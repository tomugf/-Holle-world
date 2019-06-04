#_*_coding:utf-8_*_
#分治法解决第k小的数
import random

def partition(nums):
    pi = nums[0]
    low = [x for x in nums[1:] if x < pi]
    high = [x for x in nums[1:] if x >= pi]
    return low, pi, high

# 查找第 k 小的元素
def solve(nums, k):
    low, pi,high = partition(nums)    #分解
    n = len(low) 
    if n+1 == k:    #k+1表示第k小
        return pi
    elif n < k:
        return solve(high,k-n-1) #减去小于和等于的
    else:
        return solve(low,k)

if __name__ == '__main__':
    list = [random.randint(1,20) for x in range(20)]
    print(sorted(list))
    print(solve(list,3)) #第三小
    print(solve(list,10)) #第十小