
import unittest
from red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.rb = RedBlackTree()

    def tearDown(self):
        self.rb = None

    def test_insert_empty(self):
        expect_in_order = []
        expect_level_order = []

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
    
    def test_insert_case_1(self):
        expect_in_order = [1]
        expect_level_order = [1]

        self.rb.insert(1)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
        self.assertTrue(self.rb.root.color == 'B')

    def test_insert_case_2(self):
        expect_in_order = [1, 2]
        expect_level_order = [1, 2]

        self.rb.insert(1)
        self.rb.insert(2)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
        self.assertTrue(self.rb.root.color == 'B')
        self.assertTrue(self.rb.root.right.color == 'R')

    def test_insert_case_3(self):
        expect_in_order = [1, 2, 3]
        expect_level_order = [2, 1, 3]

        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
        self.assertTrue(self.rb.root.color == 'B')
        self.assertTrue(self.rb.root.left.color == 'R')
        self.assertTrue(self.rb.root.right.color == 'R')

    def test_insert_case_4(self):
        expect_in_order = [1, 2, 3, 4]
        expect_level_order = [2, 1, 3, 4]

        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)
        self.rb.insert(4)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
        self.assertTrue(self.rb.root.color == 'B')
        self.assertTrue(self.rb.root.left.color == 'B')
        self.assertTrue(self.rb.root.right.color == 'B')
        self.assertTrue(self.rb.root.right.right.color == 'R')

    def test_insert_case_5(self):
        expect_in_order = [1, 2, 3, 4, 5]
        expect_level_order = [2, 1, 4, 3, 5]

        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)
        self.rb.insert(4)
        self.rb.insert(5)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())
        self.assertTrue(self.rb.root.color == 'B')
        self.assertTrue(self.rb.root.left.color == 'B')
        self.assertTrue(self.rb.root.right.color == 'B')
        self.assertTrue(self.rb.root.right.left.color == 'R')
        self.assertTrue(self.rb.root.right.right.color == 'R')

    def test_insert_case_large_1(self):
        expect_in_order = [1, 2, 3, 4, 5, 6, 7]
        expect_level_order = [6, 4, 7, 2, 5, 1, 3]
        self.rb.insert(7)
        self.rb.insert(6)
        self.rb.insert(5)
        self.rb.insert(4)
        self.rb.insert(3)
        self.rb.insert(2)
        self.rb.insert(1)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())

    def test_insert_case_large_2(self):
        expect_in_order = [1, 2, 3, 4, 5, 6, 7]
        expect_level_order = [2, 1, 4, 3, 6, 5, 7]

        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)
        self.rb.insert(4)
        self.rb.insert(5)
        self.rb.insert(6)
        self.rb.insert(7)

        self.assertEqual(expect_in_order, self.rb.inorder())
        self.assertEqual(expect_level_order, self.rb.levelOrder())

if __name__=='__main__':
    unittest.main()