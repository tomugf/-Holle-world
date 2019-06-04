#_*_coding:utf-8_*_
#贪心算法实例

#零钱找零,pay是应付金额
def coin(pay):
    m = [100, 25, 10, 5, 1]
    list = []

    sort_m = sorted(m, reverse=True)
    for i in sort_m:
        coin_count = int(pay/i)
        list += [i,] * coin_count
        pay -= coin_count*i
        if pay <= 0:
            break
    return list

#间隔任务， 课本改编
#规则：相同时间应听更多报告，数量相同应听更多的时间
#joblist中有['编号',开始时间，结束时间]
def best_way(joblist):
    list = []
    joblist.sort(key=lambda x : (x[1], x[2]))

    n = len(joblist)-1
    while joblist:
        if not list:
            list.append(joblist[n])
        else:
            if joblist[n][2] <= list[-1][1]:
                list.append(joblist[n])  
        n -= 1
        joblist.pop()
    list.sort(reverse=False) 
    return list

def main():
    #硬币找零
    pay = 263
    print(coin(pay))

    #间隔任务
    joblist = [['a', 1, 2], ['b', 1, 3], ['c', 2, 3], ['d', 3, 5], ['e', 3, 6], ['f', 6, 9]]
    print(best_way(joblist)) 
   

if __name__ == "__main__":
    main()