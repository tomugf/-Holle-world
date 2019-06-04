#_*_coding:utf_8_*_

import math
import random


#计算最近距离的简单算法
def min_distance(X, n):
    min_d = distance(X[0], X[1])
    min_p = [X[0], X[1]]
    for i, (x,y) in enumerate(X):    #枚举
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_p = [X[i], X[j]]      #具体的点
                min_d = distance(X[i], X[j])

    return min_p, min_d  #min_p:点坐标   min_d:距离

def distance(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2) + math.pow(a[1]-b[1], 2))

#空间中最近距离主函数
def closest(P, n):
    X = list(P)         #将元组转为列表
    Y = list(P)
    X.sort()            #(x,y)按照x进行排序吗
    Y = sort_y(Y)       #(x,y)按照y进行排序

    return closest_pair(X, Y, n)

def closest_pair(X, Y, n):
    if n <= 3:
        return brute_force(X, n)
    mid = n // 2
    Y_left = []
    Y_right = []
    for p in Y:
        if p in X[:mid]:
            Y_left.append(p)
        else:
            Y_right.append(p)
    dis_left = closest_pair(X[:mid], Y_left, mid)
    dis_right = closest_pair(X[mid:], Y_right, n-mid)
    min_dis = min(dis_left, dis_right)
    strip = []
    for (x,y) in Y:
        if abs(x-X[mid][0]) < min_dis:
            strip.append((x,y))
    return min(min_dis, strip_closest(strip, min_dis))

#处理边界内最近点对
def strip_closest(strip, d):
    min_d = d
    for i, (x,y) in enumerate(strip):
        for j in range(i+1, 8):    #只需要最多考虑7个点
            if i+j < len(strip):
                temdis = distance(strip[i], strip[j])
                if temdis < min_d:
                    min_d = temdis
    return min_d

#按照y轴距离进行排序
#sorted():key可传入一个自定义函数，表示对二维或多维中的哪一个参数进行排序
def sort_y(tuples):
    return sorted(tuples, key = lambda last: last[-1])   

#当点数小于3时，直接计算最小距离
def brute_force(X, n):
    min_d = distance(X[0], X[1])
    for i, (x, y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])
    return min_d

def main():
    A = [(round(random.uniform(1.0,10.0), 2) , round(random.uniform(1.0,10.0), 2)) for x in range(7)] #round()控制小数点位数
    min_pp, min_dd = min_distance(A, 6) 
    print("七个点的坐标："+str(A))
    print("distance:"+str(round(min_dd, 2))+", (x,y)="+str(min_pp))
    print(round(closest(A,7),2))


if __name__ == '__main__':
    main()
    


