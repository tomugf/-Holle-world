#_*_coding:utf-8_*_

import random
#选择排序递归实现
def sel_sort_rec(list,n):
    if n == 0:
        return
    max_j = n
    for j in range(n):
        if list[j] > list[max_j]:
            max_j = j
    list[n], list[max_j] = list[max_j], list[n]
    sel_sort_rec(list,n-1)
#选择排序循环实现
def sel_sort(list):
    for i in range(len(list)):
        min_j = i
        for j in range(i+1,len(list)):
            if list[min_j] > list[j]:
                min_j = j
        list[min_j], list[j] = list[min_j], list[j]

#插入排序递归实现
def ins_sort_rec(list,n):
    if n == 0:
        return
    ins_sort_rec(list,n-1)
    j = n
    while j > 0 and list[j-1] >list[j]:
        list[j-1], list[j] = list[j], list[j-1]
        j -= 1

#插入排序循环实现
def ins_sort(list):
    for i in range(1,len(list)):
        j = i
        while j > 0 and list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1

#递归的合并排序实现
def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    leftA = A[:middle]
    rightA = A[middle:]
    leftA_sorted = merge_sort(leftA)
    rightA_sorted = merge_sort(rightA)
    return merge(leftA_sorted,rightA_sorted)

#合并两个已经排序的序列
def merge(left, right):
    i, j = 0, 0
    alist = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist.append(left[i])
            i += 1
        else:
            alist.append(right[j])
            j += 1
    while i < len(left):   #左边剩余数据处理
        alist.append(left[i])
        i += 1
    while j < len(right):  #右边剩余数据处理
        alist.append(right[j])
        j += 1
    return alist




def main():
    list = [random.randint(1,10) for x in range(10)]
    sel_sort_rec(list,9)
    print("选择排序递归实现："+str(list))
    sel_sort(list)
    print("选择排序循环实现："+str(list))
    merge_sort(list)
    print("合并排序实现结果："+str(list))


if __name__ == '__main__':
    main()
