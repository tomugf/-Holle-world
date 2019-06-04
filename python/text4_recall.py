#_*_coding:utf-8_*_
#回溯算法
#参考链接: https://www.cnblogs.com/franknihao/p/9416145.html
#参考链接: https://blog.csdn.net/bajin7353/article/details/81229268

#问题1: 八皇后问题  在8X8格的国际象棋上摆放八个皇后（棋子），使任意两个皇后都不能处于同一行、同一列或同一斜线上。
#       分析   在同一斜线上可以表示为 x-y == x1-y1, 然后递归进行实现
#问题2: 求子集  已知一组数（其中无重复元素），求这组数可以组成的所有子集。结果中无重复的自己
#       分析   对于每个元素，都有试探放入或不放入集合中两种选择： 进行递归实现

import sys
import copy

#问题1
# board下标本身就代表了board中的某一行，然后值是指这一行中皇后放在第几列。raw是行，col是列，是下一个皇后要放的位置
def check(board, row, col):  
    i = 0
    while i < row:
        if abs(col-board[i]) in (0, abs(row-i)):    #在同一列或者同一斜线上
            return False
        i += 1
    return True


def EightQueen(board, row):        #raw表示从第几行开始放
    length = len(board)
    if row == length:             #表示每行都已经进行完毕
        print(board)
        return True
    col = 0
    while col < length:
        if check(board,row,col):
            board[row] = col
            if EightQueen(board,row+1):
                return True
        col += 1
    return False

def printBoard(board):
    for col in board:
        sys.stdout.write('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
        print('')

#问题2
class Solution:
    def generate(self,i,nums,result,item,):
        if i >= len(nums):
            return
        item.append(nums[i])
        item_new = copy.copy(item)   # copy.copy(x) 浅copy
        result.append(item_new)
        self.generate(i+1,nums,result,item)
        item.pop(-1)
        self.generate(i+1,nums,result,item)

    def subset(self,nums):
        result = []
        item = []

        self.generate(0,nums,result,item)
        return result

if __name__ == "__main__":
    #问题1
    board = [0] * 8
    EightQueen(board, 0)
    printBoard(board)
    #问题2
    S = Solution()
    list = [1,2,3]
    result = S.subset(list)
    print(result)