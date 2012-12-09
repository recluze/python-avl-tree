import random
import unittest
from simple_avl import AVLTree

class TestSimpleAVL(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.testelems = 1000
        self.seq = range(self.testelems) 
        
        
    def test_insert(self):
        print '----- Testing INSERTION --------'
        random.shuffle(self.seq)
        for i in self.seq: 
            self.tree.insert(i)
            
        print "Input            :", self.seq 
        print "Inorder traversal:", self.tree.inorder_traverse() 
        self.assertEqual(self.tree.inorder_traverse(), range(self.testelems))
        self.assertTrue(self.tree.check_balanced())
        
        
    def test_delete(self):
        print '----- Testing Deletion --------'
        for count in range(100): 
            print 'Iteration:', count 
            random.shuffle(self.seq)
            for i in self.seq: 
                self.tree.insert(i)
            
            # Delete a few elements and save them in a list
            deleitems = [] 
            for i in range(2): 
                item = random.randrange(0,self.testelems)
                while item in deleitems: 
                    item = random.randrange(0,self.testelems)
                self.tree.delete(item)
                deleitems.append(item)
                
    
            # print "Input            :", self.seq 
            # print "Inorder traversal:", self.tree.inorder_traverse() 
            benchmark = range(self.testelems)
            
            print deleitems 
            
            for i in deleitems: 
                benchmark.remove(i)
                
            self.assertEqual(self.tree.inorder_traverse(), benchmark)
            
            # we'll do this later 
            self.assertTrue(self.tree.check_balanced())
        
        