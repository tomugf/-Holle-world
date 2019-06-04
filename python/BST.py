#_*_coding:utf-8_*_

import random
# BST树的节点类
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# BST树及其各种操作
class BST:
    def __init__(self, *args):
        self.Root = None
    
    def find(self, key, *args):      #边界条件作用：不断找根节点赋值给start，为空时start=None
        if len(args) == 0: 
            start = self.Root
        else:
            start = args[0] 
        if not start:           #如果没有节点，则返回None
            return None 

        #如果根节点存在，则比较key值，遵循BST的右大左小规律递归查询
        if key == start.key: #找到则返回该节点
            return start
        elif key > start.key: #大于向右转
            return self.find(key, start.right)
        else: #小于向左转
            return self.find(key, start.left)
    
    def insert(self, key, *args):  # *args 用来将参数打包成tuple给函数体调用
        if not self.Root: 
            self.Root = Node(key)     #当前节点作为根节点
        elif len(args) == 0:          #查找当前节点是否存在,不存在则执行插入操作
            if not self.find(key, self.Root): #从根节点开始查，没找到返回None
                self.insert(key, self.Root) #既然没找到，那就插入操作吧
        else:            
            child = Node(key)      #用节点类创建孩子节点
            parent = args[0]             #找到当前根节点，设置为双亲节点
            if child.key > parent.key:   #比较key值，大于则向右转
                if not parent.right: 
                    parent.right = child
                    child.parent = parent
                else: 
                    self.insert(key, parent.right)
            else: #小于则向左转
                if not parent.left:
                    parent.left = child
                    child.parent = parent
                else:
                    self.insert(key, parent.left)

    def pot(self, *args):
        if len(args) == 0:
            nodes = []
            node = self.Root
        else:
            node = args[0]
            nodes = args[1]
        if node.left:
            self.pot(node.left, nodes)
        if node.right:
            self.pot(node.right, nodes)
        nodes.append(node.key)
        return nodes

    def trimBST(self, minVal, maxVal, *args):
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]
            
        if not node:
            return
        node.left = self.trimBST(minVal, maxVal, node.left)
        node.right = self.trimBST(minVal, maxVal, node.right)
        if minVal <= node.key <= maxVal:
            return node
        if node.key < minVal:
            return node.right
        if node.key > maxVal:
            return node.left

def main():
    tree = BST()
    A = [random.randint(5,30) for x in range(10)]
    for i in A:
        tree.insert(i)
    print(tree.pot())
    # tree1 = tree.trimBST(5, 13)
    # print(tree1.key)


    
    

if __name__ == '__main__':
    main()                
