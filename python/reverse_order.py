#_*_coding:UTF-8_*_

import random


#逆序计算的简单算法
def count_inversions_simple(A):
    inv_count = 0
    inv_list = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                inv_count += 1
                inv_list.append([A[i],A[j]])
    return inv_count, inv_list


#逆序计算的分治算法   边排序边找逆序数
#类似归并排序，加入了逆序数计算 T(n) = 2T(n/2) + O(n) = O(nlogn)
def count_inversions_dc(A):
    if len(A) <= 1:        #边界条件
        return 0, A
    middle = len(A) // 2
    leftA = A[:middle]
    rightA = A[middle:]
    countLA, leftA = count_inversions_dc(leftA)
    countRA, rightA = count_inversions_dc(rightA)
    countLRA, mergedA = merger_and_count(leftA,rightA)
    return countLA + countRA + countLRA, mergedA


#前提：输入的A,B是有序的 
def merger_and_count(A,B):
    i, j, inv_count = 0, 0, 0
    alist = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            alist.append(A[i])
            i += 1
        else:            # A[i] > B[j] 则B[j]与A右边所有元素构成逆序
            inv_count += len(A) - i
            alist.append(B[j])
            j += 1
    while i < len(A):
        alist.append(A[i])
        i += 1
    while j < len(B):
        alist.append(B[j])
        j += 1
    return inv_count, alist



def main():
    list = [random.randint(1,10) for x in range(10)]
    sum, alist = count_inversions_dc(list)
    print(str(list))
    print("逆序数："+str(sum)+",排序后： "+str(alist))
    


if __name__ == '__main__':
    main()





















