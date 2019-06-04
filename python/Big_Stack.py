#coding=utf-8
from __future__ import print_function
import math, random
import heapq
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def max_heapify_rec(self, i):
        if (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
                print("%d-th -> %d-th node, seq is:%s" % (i, mc, self.heapList))
                self.max_heapify_rec(mc)

    def maxChild(self, i):
        leftchild = i * 2
        rightchild = i * 2 + 1
        if leftchild <= self.currentSize and self.heapList[leftchild] > self.heapList[i]:
            largest = leftchild
        else:
            largest = i
        if rightchild <= self.currentSize and self.heapList[rightchild] > self.heapList[largest]:
            largest = rightchild
        return largest

    def max_heapify(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def buildHeap(self, alist):
        mid = len(alist) // 2     #" / "  表示浮点数除法，返回浮点结果;" // " 表示整数除法,返回不大于结果的一个最大的整数
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print("The initial seq is %s:" % self.heapList)
        while (mid > 0):
            self.max_heapify_rec(mid)
            mid = mid - 1
        return self

def heapsort(alist):
    sortedh = []
    heapq.heapify(alist)
    while alist:
        sortedh.append(heapq.heappop(alist))
    return sortedh

def print_tree(array):
    index = 1
    depth = math.ceil(math.log(len(array), 2))
    sep = ' '
    for i in range(int(depth)):
        offset = 2 ** i      #数学运算中， *为乘，**为次方,Python前缀中，（*）会把接收到的参数形成一个元组，而（**）则会把接收到的参数存入一个字典
        print(sep * (2 ** (int(depth) - i - 1) - 1), end = ' ')
        line = array[index:index+offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end = ' ')
            interval = 0 if i == 0 else 2 ** (int(depth) - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end = ' ')
        index += offset
        print()

A = [random.randint(3,40) for x in range(10)]
bh = BinHeap()
bh.buildHeap(A)
print_tree(bh.heapList)

