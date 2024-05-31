from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


tree = TreeNode(val=0,
                left=TreeNode(val=1,
                              left=TreeNode(val=3,
                                            left=TreeNode(val=7),
                                            right=TreeNode(val=8)),
                              right=TreeNode(val=4)),
                right=TreeNode(val=2,
                               left=TreeNode(val=5,
                                             left=TreeNode(val=9)),
                               right=TreeNode(val=6,
                                              left=TreeNode(val=10),
                                              right=TreeNode(val=11))))

Solution().maxDepth(tree)
