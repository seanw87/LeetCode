from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class WrongSolution:
    """
    WRONG SOLUTION!!!
    --- List in recursion seems global
    """
    @staticmethod
    def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, targetNum, curList: deque):
            if not node:
                return

            print("list sum:", sum(curList),
                  "-- node val:", node.val,
                  "-- target sum:", targetSum,
                  "-- current list:", curList)
            while ((sum(curList) + node.val) > targetSum) and len(curList) > 0:
                curList.popleft()
            if (sum(curList) + node.val) == targetSum:
                count[0] += 1
            else:
                curList.append(node.val)

            dfs(node.left, targetNum, curList)
            dfs(node.right, targetNum, curList)

        count = [0]
        dfs(root, targetSum, deque([]))

        return count[0]


class Solution2:
    """
    From each node, recursively traverse the rest nodes on the path to check if meeting the sum criteria
    Very unefficient in TC
    Efficient in SC
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.numTarget = 0

        def dfs(node, target):
            if not node:
                return

            test(node, target)

            dfs(node.left, target)
            dfs(node.right, target)

        def test(node, target):
            if not node:
                return

            if node.val == target:
                self.numTarget += 1

            test(node.left, target - node.val)
            test(node.right, target - node.val)

        dfs(root, targetSum)
        return self.numTarget


class Solution3:
    """
    Best solution.
    TC: O(n)
    cache = {pathSum: 1}
    if node a.val + b.val + c.val - target in cache, then
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # define global result and path
        self.result = 0
        cache = {0: 1}

        self.dfs(root, targetSum, 0, cache)

        return self.result

    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return

        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1


tree = TreeNode(val=10,
                left=TreeNode(val=5,
                              left=TreeNode(val=3,
                                            left=TreeNode(val=3),
                                            right=TreeNode(val=-2)),
                              right=TreeNode(val=2, right=TreeNode(val=1))),
                right=TreeNode(val=-3,
                               right=TreeNode(val=11)))

tree2 = TreeNode(val=1,
                 left=TreeNode(val=3,
                               left=TreeNode(val=7)))

print(Solution2().pathSum(tree2, 8))
