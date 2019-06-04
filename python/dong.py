#_*_coding:utf-8_*_
#动态规划
import numpy as np 
import random

#斐波那契函数
memo = {}   #字典
def fib2(n):
    if n in memo:
        return memo[n]
    else:
        if n <= 2:
            f = 1
        else:
            f = fib2(n-1) + fib2(n-2)
        memo[n] = f
        return f

def fib_bottom_up(n):
    fib = {}             #存储结果的字典
    for k in range(n+1):
        if k <= 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]   #填表
        fib[k] = f

    return fib[n]


#捡硬币
#自底向上实现递归策略
def bottom_up_coins(row_coins):
    table = [None] * (len(row_coins) + 1)    #申明表格
    table[0] = 0
    table[1] = row_coins[0]
    for i in range(2, len(row_coins)+1):
        table[i] = max(table[i-2] + row_coins[i-1], table[i-1])  #填表
    return table

#回溯
def trace_back_coins(row_coins, table):
    select = []
    i = len(row_coins)     #从最后一位索引
    while i >= 1:
        if table[i] > table[i-1]:
            select.append(row_coins[i-1])
            i -= 2
        else:
            i -= 1
    return select



#子序列和的最大值
def num_max(alist):    #自底向上递归
    table = [None] * (len(alist)+1)      
    table[0] = 0
    for i in range(1, len(alist)+1):
        table[i] = max(table[i-1] + alist[i-1], alist[i-1])  #计算重新开始的优劣
    return table

def tract_back_subseq(alist, table):
    select = []
    ind_max = np.argmax(table)        #得到最大值索引
    while ind_max >= 1:
        if table[ind_max] == alist[ind_max-1] + table[ind_max-1]:
            select.append(alist[ind_max-1])
            ind_max -= 1
        else:
            select.append(alist[ind_max-1])
            break
    return select


if __name__ == "__main__":
    list = [random.randint(1,20) for x in range(10)]
    print(list)
    print(fib2(10))
    print(fib_bottom_up(10))

    table = bottom_up_coins(list)
    print(trace_back_coins(list, table))

    table = num_max(list)
    print(tract_back_subseq(list, table))
    

