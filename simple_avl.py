#import random, math

def debug(msg):
    print msg

class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None 
        self.left = None 
        self.right = None 
        self.height = 0 
        
    def __str__(self):
        return str(self.key) + "(" + str(self.height) + ")"
    
    def is_leaf(self):
        return (self.height == 0)
    

class AVLTree():
    def __init__(self, *args):
        self.rootNode = None 
        self.elements_cound = 0 
        self.rebalance_count = 0 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.rootNode: 
            return self.rootNode.height 
        else: 
            return 0 
    
    def insert(self, key):
        tree = self.rootNode
        
        newnode = Node(key)
        
        if tree == None:
            self.rootNode = newnode 
            self.rootNode.left = AVLTree() 
            self.rootNode.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.left.insert(self, key)
            
        elif key > tree.key: 
            self.insert(self, key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")



if __name__ == "__main__": 
    a = AVLTree() 
    a.insert(2)
    a.insert(2)
    
