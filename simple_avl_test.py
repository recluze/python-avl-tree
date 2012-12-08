import random
import unittest
from simple_avl import AVLTree

class TestSimpleAVL(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.seq = range(100) 
        
    def test_insert(self):
        random.shuffle(self.seq)
        for i in self.seq: 
            self.tree.insert(i)
            
        print "Input            :", self.seq 
        print "Inorder traversal:", self.tree.inorder_traverse() 
        self.assertEqual(self.tree.inorder_traverse(), range(100))