
# (**) Rules That Every Red-Black Tree Follows: 
# 1. Every node has a color either red or black.
# 2. The root of the tree is always black.
# 3. There are no two adjacent red nodes (A red node cannot have a red parent or red child).
# 4. Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.
# All leaf nodes are black nodes (NULL).

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val: int, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.color = 'R'
        self.parent = None
        

class RedBlackTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        node = TreeNode(val)
        self.root = self._insert(self.root, node)
        self._fix_violation(node)

    def inorder(self) -> List[int]:
        return self._inorder(self.root)

    def level_order(self) -> List[int]:
        ret = []

        if not self.root:
            return []

        queue = deque()
        queue.append(self.root)

        while queue:
            k = len(queue)
            for _ in range(k):
                node = queue.popleft()
                ret.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ret
        
    def _inorder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        left = self._inorder(root.left)
        if left:
            ret.extend(left)

        ret.append(root.val)

        right = self._inorder(root.right)
        if right:
            ret.extend(right)
        
        return ret

    #     r             R
    #   L   R   ->    r   Y
    #      X Y       L X 
    def _rotate_left(self, node: TreeNode) -> TreeNode:
        r = node
        R = node.right
        X = node.right.left
        
        node = R
        R.parent = r.parent

        # need to fix new node's parent connection
        if R.parent == None:
            self.root = R
        elif R.parent.left == r:
            R.parent.left = R
        else:
            R.parent.right = R

        R.left = r
        r.parent = R
        r.right = X
        if X:
            X.parent = r

        return node
        
    #     r             L
    #   L   R   ->    X   r
    #  X Y               Y R
    def _rotate_right(self, node: TreeNode) -> TreeNode:
        r = node
        L = node.left
        Y = node.left.right

        node = L
        L.parent = r.parent

        # need to fix new node's parent connection
        if L.parent == None:
            self.root = L
        elif L.parent.left == r:
            L.parent.left = L
        else:
            L.parent.right = L

        L.right = r
        r.parent = L
        r.left = Y
        if Y:
            Y.parent = r

        return node

    def _insert(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if not root:
            return node

        if root.val > node.val:
            root.left = self._insert(root.left, node)
            root.left.parent = root
        elif root.val < node.val:
            root.right = self._insert(root.right, node)
            root.right.parent = root

        return root

    def _fix_violation(self, node: TreeNode):
        parent = None
        grand_parent = None

        while node != self.root and node.color != 'B' and node.parent.color == 'R':
            parent = node.parent
            grand_parent = node.parent.parent

            # case A:
            #   parent of node is left child of grand prant of node
            #      G
            #     / \
            #    F   U
            if parent == grand_parent.left:
                uncle = grand_parent.right
                # case: 1
                #   the uncle of node is also red => only need recoloring
                if uncle and uncle.color == 'R':
                    grand_parent.color = 'R'
                    parent.color = 'B'
                    uncle.color = 'B'
                    node = grand_parent
                else:
                    # case: 2
                    #   node is right child of its parent => left-rotate
                    #      G            G
                    #     / \          / \
                    #    F   U   ->   F   U
                    #     \          /
                    #      N        N <- node
                    if node == parent.right:
                        self._rotate_left(parent)
                        node = parent
                        parent = node.parent
                    # case: 3
                    #   node is left child of its parent => right-rotate
                    #      G            F <- node
                    #     / \          / \
                    #    F   U   ->   N   G
                    #   /                  \
                    #  N                    U
                    self._rotate_right(grand_parent)
                    grand_parent.color = 'R'
                    parent.color = 'B'
                    node = parent
            # case B:
            #   parent of node is right child of grand prant of node
            #      G
            #     / \
            #    U   F
            elif parent == grand_parent.right:
                uncle = grand_parent.left
                # case: 1
                #   the uncle of node is also red => only need recoloring
                if uncle and uncle.color == 'R':
                    grand_parent.color = 'R'
                    parent.color = 'B'
                    uncle.color = 'B'
                    node = grand_parent
                else:
                    # case: 2
                    #   node is left child of its parent => right-rotate
                    #      G            G
                    #     / \          / \
                    #    U   F   ->   U   F
                    #       /              \
                    #      N                N <- node
                    if node == parent.left:
                        self._rotate_right(parent)
                        node = parent
                        parent = node.parent
                    # case: 3
                    #   node is left child of its parent => right-rotate
                    #      G             F <- node
                    #     / \           / \
                    #    U   F   ->    G   N
                    #         \       /            
                    #          N     U       
                    self._rotate_left(grand_parent)
                    grand_parent.color = 'R'
                    parent.color = 'B'
                    node = parent


        self.root.color = 'B'

if __name__ == '__main__':
    rb_tree = RedBlackTree()
    rb_tree.insert(7)
    rb_tree.insert(6)
    rb_tree.insert(5)
    rb_tree.insert(4)
    rb_tree.insert(3)
    rb_tree.insert(2)
    rb_tree.insert(1)

    print(rb_tree.inorder())
    print(rb_tree.level_order())