# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def goodNodes(root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, cur_max):
            if not node:
                return

            if node.val >= cur_max:
                count[0] += 1
                cur_max = node.val

            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        count = [0]
        dfs(root, root.val)

        return count[0]


class Solution2:
    def goodNodes(self, root: TreeNode, ma=-10000):
        return (
                self.goodNodes(root.left, max(ma, root.val)) +
                self.goodNodes(root.right, max(ma, root.val)) +
                (root.val >= ma)
                ) if root else 0


tree = TreeNode(val=3,
                left=TreeNode(val=1,
                              left=TreeNode(val=3)),
                right=TreeNode(val=4,
                               left=TreeNode(val=1,
                                             right=TreeNode(val=5))))

print(Solution2().goodNodes(tree))