
from typing import List


class SegmentTreeNode:
    def __init__(self, start: int, end: int, val: int, left = None, right = None) -> None:
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right
        self.tag = 0
        
    def get_value(self) -> int:
        if self.tag > 0:
            return self.tag * (self.end - self.start + 1)
        return self.val

class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.root = None

        if nums:
            self.root = self._build(nums, 0, len(nums)-1)
    
    def update(self, i: int, val: int):
        self._update_range(self.root, i, i, val)

    def update_range(self, l: int, r: int, val: int):
        self._update_range(self.root, l, r, val)

    def query(self, l: int, r: int):
        return self._query(self.root, l, r)

    def _build(self, nums: List[int], start: int, end: int) -> SegmentTreeNode:
        if start == end:
            return SegmentTreeNode(start, end, nums[start])

        m = start + (end - start) // 2
        left = self._build(nums, start, m)
        right = self._build(nums, m+1, end)
        # custom logic (sum)
        return SegmentTreeNode(start, end, left.val + right.val, left, right)

    def _update(self, root: SegmentTreeNode, i: int, val: int) -> bool:
        # find leaf node
        if root.start == root.end:
            if root.start == i:
                root.val = val
                return True
            return False
        
        m = root.start + (root.end - root.start)//2
        # in left node
        if i <= m:
            if not self._update(root.left, i, val):
                return False
        # in right node
        else:
            if not self._update(root.right, i, val):
                return False
        # custom logic (sum)
        root.val = root.left.val + root.right.val
        return True

    def _update_range(self, root: SegmentTreeNode, l: int, r: int, val: int) -> bool:

        # out of range
        if l > root.end or r < root.start:
            return

        # full match in range
        # Lazy Propagation 
        if l <= root.start and root.end <= r:
            # custom logic (sum)
            root.tag = val
            return

        self._push(root)
        self._update_range(root.left, l, r, val)
        self._update_range(root.right, l, r, val)
        # custom logic (sum)
        root.val = root.left.get_value() + root.right.get_value()

        
    def _query(self, root: SegmentTreeNode, l: int, r: int) -> int:
        # out of range
        if l > root.end or r < root.start:
            return 0

        # full match in range
        if root.start >= l and root.end <= r:
            return root.get_value()

        self._push(root)
        # custom logic (sum)
        return self._query(root.left, l, r) + self._query(root.right, l, r)

    def _push(self, root: SegmentTreeNode):
        # has mark
        if root.tag > 0:
            root.left.tag = root.tag
            root.right.tag = root.tag
            root.val = root.get_value()
            root.tag = 0

    def traverse(self):
        raise NotImplementedError


def main():
    arr = [1, 2, 3, 4, 5]
    st = SegmentTree(arr)
    print(st.query(0,2))
    print(st.query(1,3))
    st.update(0, 6)
    print(st.query(0,2))
    print(st.query(1,3))
    st.update_range(0, 4, 5)
    print(st.query(0,4))
    print(st.query(1,3))
    print(st.query(0,3))
    st.update(3, 10)
    print(st.query(0,4))
    print(st.query(1,3))
    print(st.query(0,3))

if __name__ == '__main__':
    main()

        
