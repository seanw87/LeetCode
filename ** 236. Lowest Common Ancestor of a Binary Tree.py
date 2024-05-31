from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ppath = ""
    qpath = ""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return

        def dfs(node, path):
            if not node:
                return

            path += str(node.val) + ","
            print(path)
            if node.val == p.val:
                self.ppath = path
            elif node.val == q.val:
                self.qpath = path

            dfs(node.left, path)

            dfs(node.right, path)

        dfs(root, "")
        print(self.ppath[:-1], self.qpath[:-1])
        plist = self.ppath[:-1].split(",")
        qlist = self.qpath[:-1].split(",")
        # # ↓ still not fast
        # qset = set(qlist)
        # first_common = next((plist[i] for i in range(len(plist)-1, -1, -1) if plist[i] in qset), None)
        # return TreeNode(val=first_common)
        # # ↑ still not fast

        # # ↓ O(n^2) needs to be optimized
        # for i in range(len(plist)-1, -1, -1):
        #     for j in range(len(qlist)-1, -1, -1):
        #         if plist[i] == qlist[j]:
        #             print(plist[i])
        #             return TreeNode(val=plist[i])
        # # ↑ O(n^2) needs to be optimized


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:  # if another node(e.g. q) is node p's descendant, then the result is p
            return right
        elif right is None:  # same as above
            return left
        else:  # if both node p and q are found, which means they are from another parent node, which is root
            return root


tree = TreeNode(val=3,
                left=TreeNode(val=5,
                              left=TreeNode(val=6),
                              right=TreeNode(val=2,
                                             left=TreeNode(val=7),
                                             right=TreeNode(val=4))),
                right=TreeNode(val=1,
                               left=TreeNode(val=0),
                               right=TreeNode(val=8)))

tree2 = TreeNode(val=-1,
                 left=TreeNode(val=0,
                               left=TreeNode(val=-2,
                                             left=TreeNode(val=8)),
                               right=TreeNode(val=4)),
                 right=TreeNode(val=3))

print(Solution().lowestCommonAncestor(tree2, TreeNode(val=3), TreeNode(val=8)))
