#_*_coding:utf-8_*_
#分治算法
#问题1: 利用分治法排序
#问题2: 给定一个顺序表，编写一个求出其最大值的分治算法。
import random

#问题1，倒着进行排序
def separate_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = separate_sort(array[:middle])    #分治求解
    right = separate_sort(array[middle:])
    
    res = []
    while left and right:            
        if left[-1] >= right[-1]:     #尾部较大者
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()   #倒序
    return (left or right) + res     #前面加上剩下的非空nums

#问题2
def solve(list):
    n = len(list)
    if n <= 2:           
        return max(list)

    left_list, right_list = list[:n//2], list[n//2:]
    left_max  = solve(left_list)
    right_max = solve(right_list)
    
    return max([left_max, right_max])


if __name__ == "__main__":
    list = [random.randint(1,20) for x in range(10)]
    print("原列表："+str(list))
    # 求最大值
    print("最大值：", end="")
    print(solve(list))  # 67
    #排序之后
    print("排序后：", end="")
    print(separate_sort(list))
   
  
  