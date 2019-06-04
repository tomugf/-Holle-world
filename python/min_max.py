import time
 
Max = -99999
Min = 99999
 
def getMax_Min(arr,left,right):
    global Max,Min          #=为一个定义在函数外的变量赋值,定义全局的变量,我们使用global语句完成这一功能
    left = int(left)
    right = int(right)
    if right - left <=1:
        if(arr[left] < arr[right]):
            if Max < arr[right]:
                Max = arr[right]
            if Min > arr[left]:
                Min = arr[left]
        else:
            if Max < arr[left]:
                Max = arr[left]
            if Min > arr[right]:
                Min = arr[right]
    else:
        mid  = (right - left)/2 + left
        getMax_Min(arr,left,mid)
        getMax_Min(arr,mid,right)
 
def main():
    list = [5, 2, 6, 3, 9, 8]
    left = 0
    right = len(list) - 1
    getMax_Min(list,left,right)
    print("MAX = %d"%Max)
    print("Min = %d"%Min)
   
 
if __name__ == '__main__':
    main()
 
 
 
 
 
 