
import unittest
from red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.rb = RedBlackTree()

    def tearDown(self):
        self.rb = None

    def test_insert(self):
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


if __name__=='__main__':
    unittest.main()