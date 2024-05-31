from typing import Optional, List
from math import sqrt, floor, pow


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class WrongSolution:
    """
    try to store the layer # in a hash by numbering the nodes, but nodes may not exist.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        node_pointer = 1
        layer_hit = {}

        nq = [(root, node_pointer)]
        res = []

        while nq:
            node = nq.pop(0)
            layer = floor(sqrt(node[1])) if node[1] > 1 else 0
            if layer not in layer_hit:
                res.append(node[0].val)
                layer_hit[layer] = True

            node_pointer += 1
            if node[0].right:
                nq.append((node[0].right, node_pointer))
            node_pointer += 1
            if node[0].left:
                nq.append((node[0].left, node_pointer))

        return res


class Solution:
    """
    DFS solution: since each layer return the right most node,
    so the size of the result can be regarded as the total layers.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def dfs(node, curDepth):
            if not node:
                return

            if curDepth == len(res):
                res.append(node.val)

            dfs(node.right, curDepth+1)
            dfs(node.left, curDepth+1)

        dfs(root, 0)
        return res


class Solution2:
    """
    combine right and left:
    for the branch of each layer, get the right most node, if not existed, get the left node(left[len(right):])
    [root.val]: [4] right: [] left: []
    [root.val]: [5] right: [] left: [4]
    [root.val]: [2] right: [] left: []
    [root.val]: [3] right: [5, 4] left: [2]
    [root.val]: [1] right: [3, 5, 4] left: []
    [root.val]: [6] right: [] left: [1, 3, 5, 4]

    TC: O(n^2) (list concatenation in return is O(n^2))
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)

        print("[root.val]:", [root.val], "right:", right, "left:", left)

        return [root.val] + right + left[len(right):]


class Solution3:
    """
    BFS solution: iterate each layer
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            level = [root]
            while level:
                res.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]

        return res


tree = TreeNode(val=6)
tree.left = TreeNode(val=1)
tree.left.right = TreeNode(val=3)
tree.left.right.left = TreeNode(val=2)

tree.left.right.left.left = TreeNode(val=100)
tree.left.right.left.right = TreeNode(val=101)

tree.left.right.right = TreeNode(val=5)
tree.left.right.right.left = TreeNode(val=4)

print(Solution3().rightSideView(tree))
