import unittest
from binaryTree import BinarySearchTree

class BSTTestCase(unittest.TestCase):
    def test_bstTest(self):
        bst=BinarySearchTree()

        #Test 'add' and 'size'

        bst.add(10, "A value")
        self.assertEqual(bst.size(),1)

        bst.add(5, "B value")
        self.assertEqual(bst.size(),2)

        bst.add(30, "C value")
        self.assertEqual(bst.size(),3)

        #Test inorder_Walk

        self.assertEqual(bst.inorder_walk(), [5,10,30])

        bst.add(15, "Value")
        self.assertEqual(bst.inorder_walk(), [5,10,15,30])

        #Test preorder_Walk

        self.assertEqual(bst.preorder_walk(), [10,5,30,15])

        #Test postorder_Walk
        self.assertEqual(bst.postorder_walk(), [5,15,30,10])

        #Test smallest key
        self.assertEqual(bst.smallest(),5)

        #Test largest key
        self.assertEqual(bst.largest(),30)

        #Test search
        self.assertEqual(bst.searche(5), True)
      
        


if __name__=='__main__':
    unittest.main()
        

        
