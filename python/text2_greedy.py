#_*_coding:utf-8_*_
#贪心算法
#参考链接: https://blog.csdn.net/wangbowj123/article/details/78335203
#参考链接: https://www.cnblogs.com/zf-blog/p/8674932.html

#问题1: 一辆汽车加满油后可行驶n公里。旅途中有若干个加油站。设计一个有效算法，指出应在哪些加油站停靠加油，使沿途加油次数最少。 
#      对于给定的n(n <= 5000)和k(k <= 1000)个加油站位置，编程计算最少加油次数。
#问题2: 给定n个物品和一个容量为C的背包，物品i的重量是Wi,其价值为Vi,选择放入背包的物品，
#      使得装入背包的物品的总价值最大，可以将物品的一部分装入背包，但不能重复装入。
import random

#问题1
def car_add_oil(distance, list):     
    # distance表示汽车加满油行驶的距离，list表示加油站之间的距离

    for i in list:
        if i > distance:
            print("汽车油箱太小，换一个新车吧!!")
            return
    
    dis , num = 0, 0  #num表示第几个加油站
    add_oil = []
    for i in list:
        dis += i
        if dis > distance:
            add_oil.append(num)  #表示在第几个加油站加油
            dis = i
        num += 1
    print(add_oil)

#问题2
class goods:
    def __init__(self, goods_id, weight=0, value=0):
        self.id = goods_id
        self.weight = weight
        self.value = value


def knapsack(capacity=0, goods_list=[]):
    # 按单位价值量排序
    goods_list.sort(key=lambda obj: obj.value / obj.weight, reverse=True)
    result = []
    for a_goods in goods_list:
        if capacity < a_goods.weight:
            break
        result.append(a_goods)
        capacity -= a_goods.weight
    if len(result) < len(goods_list) and capacity != 0:
        result.append(goods(a_goods.id, capacity, a_goods.value * capacity / a_goods.weight))
    return result


def main():
    #汽车加油
    list = [random.randint(1, 100) for x in range(10) ]
    distance = 100
    print("======加油问题======")
    print("加油站距离："+ repr(list))
    print("加油的编号：", end = "")
    car_add_oil(distance, list)

    #背包问题
    some_goods = [goods(0, 2, 4), goods(1, 8, 6), goods(2, 5, 3), goods(3, 2, 8), goods(4, 1, 2)]
    res = knapsack(6, some_goods)

    print("======背包问题======")
    for obj in res:
        print('物品编号:' + str(obj.id) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.value), end=',')
        print('单位价值量为:' + str(obj.value / obj.weight))




if __name__ == '__main__':
    main()

