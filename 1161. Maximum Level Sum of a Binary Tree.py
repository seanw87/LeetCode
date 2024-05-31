from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BFS
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        maxlevel = -math.inf
        depth = 0
        res = -1

        while level:
            depth += 1

            level_sum = sum([node.val for node in level])
            if level_sum > maxlevel:
                maxlevel = level_sum
                res = depth

            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return res


class Solution2:
    """
    DFS
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        level_val = []

        def dfs(node, curDepth):
            if not node:
                return

            if len(level_val) == curDepth:
                level_val.append(node.val)
            else:
                level_val[curDepth] += node.val

            dfs(node.left, curDepth+1)
            dfs(node.right, curDepth+1)

        dfs(root, 0)

        return level_val.index(max(level_val)) + 1
