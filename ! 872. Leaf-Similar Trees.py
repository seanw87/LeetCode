from typing import Optional
from itertools import zip_longest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1. yield from (from python 3.3): 
    allowing a generator to delegate part of its operations to another generator
    For simple iterators, yield from iterable is essentially just a shortened form of for item in iterable: 
    yield item:
    >>>
    def g(x):
        yield from range(x, 0, -1)
    
    However, unlike an ordinary loop, yield from allows subgenerators to receive sent and thrown values directly 
    from the calling scope, and return a final value to the outer generator
    Or, more simply: establishes a transparent, bidirectional connection between the caller and the sub-generator
    
    https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3
    https://docs.python.org/3/whatsnew/3.3.html#pep-380
    
2. itertools.zip_longest()
"""


class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val

            yield from dfs(root.left)
            yield from dfs(root.right)

        return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))


class Solution:
    def __init__(self):
        self.leaf_nodes1 = []
        self.leaf_nodes2 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.iterTree(root1, self.leaf_nodes1)
        self.iterTree(root2, self.leaf_nodes2)
        if self.leaf_nodes1 == self.leaf_nodes2:
            return True

    def iterTree(self, root, leaf_nodes):
        if root is not None and root.left is None and root.right is None:
            leaf_nodes.append(root.val)
        if root is None:
            return

        self.iterTree(root.left, leaf_nodes)
        self.iterTree(root.right, leaf_nodes)
