#_*_coding:utf-8_*_
#date:2019-5-20
#分治法排序

def separate_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    #分治求解
    left = separate_sort(array[:middle])
    right = separate_sort(array[middle:])
    #合并
    res = []
    while left and right:            #两个都不为空的时候
        if left[-1] >= right[-1]:    #尾部较大者
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()   #倒序
    return (left or right) + res     #前面加上剩下的非空nums
   
def main():
    A = [5,4,1,2,3]
    A = separate_sort(A)
    print(A)

if __name__ == "__main__":
    main()