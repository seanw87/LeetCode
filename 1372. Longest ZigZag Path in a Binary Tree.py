from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.longestZigZag = 0

        # lr - 1:left, 2:right
        def dfs(node, lrCnt, lr):
            if not node:
                return

            # the node goes to the left, then if the parent is from right direction, then path + 1
            lcnt = lrCnt + 1 if lr == 2 else 0
            self.longestZigZag = max(lcnt, self.longestZigZag)

            dfs(node.left, lcnt, 1)

            # the node gois to the right, then if the parent is from left direction, then path + 1
            rcnt = lrCnt + 1 if lr == 1 else 0
            self.longestZigZag = max(rcnt, self.longestZigZag)

            dfs(node.right, rcnt, 2)

        dfs(root, 0, 0)

        return self.longestZigZag


class Solution2:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.longestZigZag = 0

        # lr - 1:left, 2:right
        def dfs(node, lrCnt, lr):
            self.longestZigZag = max(lrCnt, self.longestZigZag)

            if not node:
                return

            # the node goes to the left, then if the parent is from right direction, then path + 1
            lcnt = lrCnt + 1 if lr == 2 else 0
            dfs(node.left, lcnt, 1)

            # the node gois to the right, then if the parent is from left direction, then path + 1
            rcnt = lrCnt + 1 if lr == 1 else 0
            dfs(node.right, rcnt, 2)

        dfs(root.left, 0, 1)
        dfs(root.right, 0, 2)

        return self.longestZigZag