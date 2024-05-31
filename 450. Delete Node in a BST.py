from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root and root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root and root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # key found, delete the node and attach rest to the trunk
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                right_smallest = root.right
                while right_smallest.left:
                    right_smallest = right_smallest.left
                right_smallest.left = root.left
                return root.right

        return root
