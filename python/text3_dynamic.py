#_*_coding:utf-8_*_
#动态规划
#参考链接：https://www.cnblogs.com/liuyicai/p/10182262.html

#问题1: 爬楼梯， 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#       分析    到第十层可能是从第八层或第九层到第十层  ，所以f(10) = f(8) + f(9)

#问题2: 买卖股票, 给定一个数组，它的第 i 个元素是一支股票第 i 天的价格，你最多只允许完成一笔交易，计算你所能获取的最大利润
#       分析    动态填表 计算当前的最优值，max(dp[i-1], price[i]-min_value)

import random

#问题1 方法一
def staris(n):
    list = {}
    if n <= 2:
        return n 
    else:
        list[n] = staris(n-1) + staris(n-2)
    return list[n]

#问题1 方法二
def staris2(n):
    list = [0, 1, 2]
    if n <= 2:
        return n
    else:
        for i in range(3, n+1):
            list.append(list[i-1]+list[i-2])
        return list[n]

#问题2
def stock(list):
    if len(list) <= 1:
        return 0
    else:
        dp = [None] * len(list)
        dp[0] = 0
        min_value = list[0]
        for i in range(1, len(list)):
            dp[i] = max(dp[i-1], list[i] - min_value)
            if list[i] < min_value:
                min_value = list[i]
        return dp[i-1]
        

def main():
    list = [random.randint(1,15) for x in range(10)]
    #问题1
    print(staris(10))
    print(staris2(10))
    #问题2
    print(list)
    print(stock(list))


if __name__ == "__main__":
    main()